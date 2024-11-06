import streamlit as st
import streamlit.components as stc
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import StreamlitChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_community.llms import Ollama  # temp koo
from langchain.memory import StreamlitChatMessageHistory
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
#from transformers import pipeline
from config_beta_kw import *
from kwDB_st_pdfminer import make_db
import random  # 추가
import math
import os


##
def main():
	
    # 전체페이지 구성
    st.set_page_config(
        page_title="DB Creation ",
        page_icon=":classical_building:",
        initial_sidebar_state="collapsed"
    )  # 사이드바를 기본적으로 숨김 상태로 설정)

    # Title
    st.title("_DB creation (:red[k-water])_ :books:")

    def get_subdirectories(directorys):
        return [d for d in os.listdir(directorys) if os.path.isdir(os.path.join(directorys, d))]

    ##
    def button_callback(dname):
        #print(f"path = {dname}")
        make_db(dname)
        # 버튼 상태 유지를 위해 return False 추가
        return False

    st.subheader("Select folder to add to DB")
    subdirs = get_subdirectories(DOCUMENTs)

    # 한 줄에 표시할 버튼 수 계산
    buttons_per_row = 4
    total_buttons = len(subdirs)
    rows = math.ceil(total_buttons / buttons_per_row)

    for row in range(rows):
        cols = st.columns(buttons_per_row)
        for col, (index, dir_path) in enumerate(enumerate(subdirs[row*buttons_per_row:(row+1)*buttons_per_row], start=row*buttons_per_row)):
            with cols[col % buttons_per_row]:
                st.button(
                    f"{dir_path}", 
                    key=f"btn_{str(random.randint(10000, 999999))}_{hash(dir_path)}", 
                    on_click=button_callback, 
                    args=(dir_path,)
                )

if __name__ == '__main__':
	main()

