import streamlit as st
import pandas as pd
from init import client
from io import BytesIO
import os

def render_sidebar():
    with st.sidebar:

        main = st.Page(
            "page/page_main.py",
            title = "Main Page",
            icon = ":material/home:"
        )

        page_2021 = st.Page(
            "page/page_2021.py",
            title = "2021",
        ) 

        page_2022 = st.Page(
            "page/page_2022.py",
            title = "2022",
        ) 

        page_2023 = st.Page(
            "page/page_2023.py",
            title = "2023",
        ) 

        page_2024 = st.Page(
            "page/page_2024.py",
            title = "2024",
        ) 

        pages = {
            "Home" : [main],
            "K-water Informations":[
                page_2021,
                page_2022,
                page_2023,
                page_2024
            ]
        }

    
    return pages
    
vector_store_id = 'vs_46Tnl9kk9H399oAIRwj01OOS'

def handle_file_upload():
    with st.sidebar:
        uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
        if uploaded_files:
            for uploaded_file in uploaded_files:
                st.write(f"filename : {uploaded_file}")

            # 업로드된 파일을 서버에 저장
            saved_file_paths = save_uploaded_files(uploaded_files)
            st.write("파일이 서버에 저장되었습니다:", saved_file_paths)

            file_batch =upload_files_to_vector_store(vector_store_id, saved_file_paths)
            st.write(f"파일들이 백터스토어에 업로드되었습니다. \n{file_batch}")

        # for uploaded_file in uploaded_files:
        #     bytes_data = uploaded_file.read()
        #     st.write("filename:", uploaded_file.name)
        #     st.write(bytes_data)

    return uploaded_files



def upload_files_to_vector_store(vector_store_id, uploaded_files): 
    # 업로드된 파일들을 벡터스토어에 추가
    file_streams = [open(path, 'rb') for path in uploaded_files]
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store_id, 
        files=file_streams
    )

    vector_store_files = client.beta.vector_stores.retrieve(
        vector_store_id=vector_store_id,
    )
    file_ids = vector_store_files.file_counts

    
    st.write(f"저장 취소 : {file_ids.cancelled}개")
    st.write(f"저장된 파일 수: {file_ids.completed}개")
    st.write(f"저장 실패 수: {file_ids.failed}개")
    st.write(f"저장 진행 중 : {file_ids.in_progress}개")
    st.write(f"저장된 총 파일 : {file_ids.total} 개")

    return file_batch
    


# 업로드된 파일을 임시로 저장하는 함수
def save_uploaded_files(uploaded_files):
    saved_file_paths = []
    
    # 현재 작업 디렉토리의 절대 경로 가져오기
    base_path = os.path.abspath("docs")
    
    # 저장 디렉토리가 존재하지 않으면 생성
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    for uploaded_file in uploaded_files:
        # 절대 경로로 파일 저장 경로 생성
        file_path = os.path.join(base_path, uploaded_file.name)
        
        # 파일을 절대 경로로 저장
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())  # 파일 저장
        saved_file_paths.append(file_path)

    return saved_file_paths