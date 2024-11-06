import streamlit as st
import streamlit.components as stc
# from langchain.chains import ConversationalRetrievalChain
# from langchain.memory import StreamlitChatMessageHistory
# from langchain.memory import ConversationBufferMemory
# from langchain.vectorstores import Chroma
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain_community.chat_models import ChatOllama
# from langchain_community.llms import Ollama  # temp koo
# from langchain.memory import StreamlitChatMessageHistory
# from langchain.llms import HuggingFacePipeline
# from langchain.prompts import PromptTemplate
# from langchain.schema.runnable import RunnablePassthrough
# from langchain.prompts import ChatPromptTemplate
# from langchain.schema.output_parser import StrOutputParser
#from transformers import pipeline
# from config_beta_kw import *
# from kwDB_st_pdfminer import make_db
import random  # 추가
import math
import os
import time



def process_files(folder_path):
    

##
def main():
    # 전체페이지 구성
    st.set_page_config(
        page_title="DB Creation ",
        page_icon=":classical_building:",
        initial_sidebar_state="collapsed"
    )  # 사
    st.title(":blue[K-water] 수자원공사 챗봇")

    st.write("""
    K-water의 30년 이상 축적된 해외사업 정보와 사내 전문 정보 시스템에 효율적으로 접근할 수 있는 AI 챗봇입니다. \n
    연도별로 정리된 카테고리별 데이터를 활용하여, 사용자가 원하는 연도와 주제에 맞는 문서를 검색하고 신속하게 답변합니다.\n
     """)
    st.code("""
    [ 이용 방법 ]
    1. 질문 입력: 한국어로 질문을 입력하세요. 예를 들어 "2021년 (특정)해외사업 보고서 내용"과 같이 입력하면, 챗봇이 해당 연도의 관련 문서를 우선적으로 검색합니다.
    2. 결과 확인: 챗봇이 선택한 연도의 자료에서 가장 적합한 답변을 찾아 제공해줍니다. 추가적으로 더 많은 정보가 필요하면, 추가 질문을 통해 챗봇과 상호작용할 수 있습니다.

    이 챗봇은 K-water의 방대한 연도별 데이터를 체계적으로 관리하며, 사용자에게 필요한 정보를 빠르게 제공할 수 있도록 설계되어 있어 업무의 효율성을 높이는 데 도움이 됩니다.
    """)

    

    with st.sidebar:
        
    # ##
    def button_callback(dname):
        #print(f"path = {dname}")
        # make_db(dname)
        st.success(f"{dname}: DB 저장이 완료되었습니다.")
        # 버튼 상태 유지를 위해 return False 추가
        return False

    # subdirs = get_subdirectories(DOCUMENTs)

    # selected_folder = st.selectbox(label="Save only PDF files" ,options=FOLDER_LIST )

    # if st.button("DB 저장", key="main_db_save", use_container_width=True):
    #     folder_path = os.path.join(DOCUMENTs, selected_folder)
    #     process_files(folder_path)



    # # 한 줄에 표시할 버튼 수 계산
    # buttons_per_row = 4
    # total_buttons = len(subdirs)
    # rows = math.ceil(total_buttons / buttons_per_row)

    # for row in range(rows):
    #     cols = st.columns(buttons_per_row)
    #     for col, (index, dir_path) in enumerate(enumerate(subdirs[row*buttons_per_row:(row+1)*buttons_per_row], start=row*buttons_per_row)):
    #         with cols[col % buttons_per_row]:
    #             st.button(
    #                 f"{dir_path}", 
    #                 key=f"btn_{str(random.randint(10000, 999999))}_{hash(dir_path)}", 
    #                 on_click=button_callback, 
    #                 args=(dir_path,)
    #             )

if __name__ == '__main__':
	main()

