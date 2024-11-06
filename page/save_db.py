import streamlit as st
import time, os
from init import client
# from transformers import pipeline
# from config_beta_kw import *
# from kwDB_st_pdfminer import make_db


# vector_store_id = 'vs_46Tnl9kk9H399oAIRwj01OOS'



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



DOCUMENTs = "/Users/ainomis_dev/Desktop/empty"
st.title(":blue[K-water] Save PDF")
st.write("수자원공사 관련자료를 업로드하세요")

def get_subdirectories(directorys):
        return [d for d in os.listdir(directorys) if os.path.isdir(os.path.join(directorys, d))]

FOLDER_LIST = sorted(get_subdirectories(DOCUMENTs))

    
selected_folder_sidebar = st.selectbox(label="Choose folder / Save Only '.pdf'", options=FOLDER_LIST)
if st.button("파일 업로드", use_container_width=True):
    folder_path = os.path.join(DOCUMENTs, selected_folder_sidebar)
    """선택한 폴더 내의 PDF 파일 처리 함수"""
    # 선택한 폴더 내의 파일 목록 가져오기
    files = os.listdir(folder_path)  # 폴더 내의 모든 파일 및 하위 폴더 목록
    pdf_files = [file for file in files if file.lower().endswith('.pdf')]

    with st.status("작업 진행 중...", expanded=True) as status:
        for file in pdf_files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                st.write(f"{file} 처리중...")
                time.sleep(2)  # 작업 진행 시간 시뮬레이션
                st.write(f"{file} 백터화 진행...")
                time.sleep(2)  # 작업 진행 시간 시뮬레이션
                st.info(f"'{file}'의 처리가 완료되었습니다.", icon="ℹ️")
        status.update(label=f"{folder_path} 저장 완료되었습니다.", state="complete", expanded=True)
        st.success("모든 파일이 Vector DB에 저장되었습니다.")

st.write("---")


#######################################################################################

## 기본 파일 업로드 방식
uploaded_files = st.file_uploader("Choose a file", accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        st.write(f"filename : {uploaded_file}")

    # 업로드된 파일을 서버에 저장
    saved_file_paths = save_uploaded_files(uploaded_files)
    st.write("파일이 서버에 저장되었습니다:", saved_file_paths)

    file_batch =upload_files_to_vector_store(vector_store_id, saved_file_paths)
    st.write(f"파일들이 백터스토어에 업로드되었습니다. \n{file_batch}")




