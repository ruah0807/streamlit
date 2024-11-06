import streamlit as st
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from pdfminer.high_level import extract_pages 
from pdfminer.layout import LTTextContainer 
from langchain.docstore.document import Document
from config_beta_kw import *
import os
import pprint

embeddings = HuggingFaceEmbeddings(
    model_name=bgeEMBED_MODEL,
    model_kwargs={'device': 'cuda'},
    encode_kwargs={'normalize_embeddings': True}
    )

@st.cache_resource
def get_vectorstore():
    return Chroma(persist_directory=Pm_Persist_directory, embedding_function=embeddings)

def extract_text_by_page(pdf_path): 
    try:
        for page_layout in extract_pages(pdf_path): 
            page_text = "" 
            for element in page_layout: 
                if isinstance(element, LTTextContainer): 
                    page_text += element.get_text() 
            yield page_text 
    except FileNotFoundError:
        st.error(f"Error: The file '{pdf_path}' was not found.")
        return -1
    # PDF 문서 구조에 문제가 있는 경우 (잘못된 PDF 형식 등)
    except Exception as e:
        st.error(f"An unexpected error: {e}")
        return -1

##
def trim_data(mdata):
    # 경로에서 파일 이름 추출
    file_name = os.path.basename(mdata)
    # 파일 이름을 제외한 경로 추출
    dir_path = os.path.dirname(mdata)
    # 마지막 디렉토리 추출
    last_directory = os.path.basename(dir_path)
    # 마지막 디렉토리와 파일 이름을 결합하여 새로운 경로 생성
    modified_path = os.path.join(last_directory, file_name)
    return modified_path    

def pdf_reader(pdfname):
    st.markdown(f"👉 : {trim_data(pdfname)}", unsafe_allow_html=True)
    
    documents = []
    for page_num, page_text in enumerate(extract_text_by_page(pdfname), start=1): 
        # 페이지 번호와 파일명을 메타데이터로 추가하여 문서 생성
        if page_text == -1:
            return page_text
        metadata = {"page": page_num, "source": pdfname}
        #pprint.pprint(f'page === {page_num} \n {page_text}')
        documents.append(Document(page_content=page_text, metadata=metadata))   
    #pprint.pprint(f'pdfminer = {documents.page_content}')
    text_splitter = RecursiveCharacterTextSplitter(chunk_size= CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    texts = text_splitter.split_documents(documents)
    return texts

##
def db_input(fname):
    file_ext = os.path.splitext(fname)[-1].lower()  # 파일 확장자(.pdf)
    # extension = extensions.get(file_ext)  

    if os.path.isdir(Pm_Persist_directory):  # db가 이미 생성되어있는가?
        _vectordb = get_vectorstore()
        result = _vectordb.get(where={'source':  fname })
        if 'ids' in result and result['ids']:
           st.markdown(f'👉 : {trim_data(fname)} __embedded !!', unsafe_allow_html=True)
           return False
    else:
        st.markdown(f"**DB 최초 생성** : {Pm_Persist_directory}")

    if file_ext == ".pdf":
        texts = pdf_reader(fname)
        if texts == -1:
            return False
    else:
        st.error("file corruption")
        return False

    try:
        with st.spinner("DB creation in progress...."):
            Chroma.from_documents(
                documents=texts,
                embedding=embeddings,
                persist_directory=Pm_Persist_directory)
            return True
    except Exception as e:
        st.error(f"DB write 오류:{fname} : {e}")
        return False

##
def read_docs_in_directory(directory):
    # extensions = [".pdf", ".hwp", ".csv"]
    extensions = [".pdf"]    # CSV 파일 DB는 별도로 생성함
    # 현재 작업 디렉토리에 모든 파일 찾기
    f_count = 0
    for file in os.listdir(directory):
        file_ext = os.path.splitext(file)[-1].lower()
        if file_ext in extensions:
            docs_file = os.path.join(directory, file)
            if db_input(docs_file) == True:
                f_count += 1
                st.markdown(f'success __{str(f_count)} ')
        else:
            st.error(f"파일 형식오류 : {file}")
            continue
    return f_count

##
def make_db(dir_name):
    full_path = os.path.join(DOCUMENTs, dir_name)
    file_num = read_docs_in_directory(full_path)
    #result_p.markdown(f'디렉토리 :blue[{full_path}] __파일 {str(file_num)}개 DB에 추가됨.')
    st.markdown(f'☰ :blue[디렉토리 {full_path}] __파일 {str(file_num)}개 DB에 추가됨.')

