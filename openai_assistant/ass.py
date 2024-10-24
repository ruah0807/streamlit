import os,sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from openai import OpenAI
from dotenv import load_dotenv
from init import client

load_dotenv()

ass_id = 'asst_ifqkPUog6RMvmWD27YYGFS9M'
# [Assistant Name]: Test ChatBot🤖, [Assistant ID] : asst_ifqkPUog6RMvmWD27YYGFS9M


instructions = """
[ Role ]
    당신은 K-water Test chatbot 입니다.
"""


# Chatbot
# vector_store = client.beta.vector_stores.update(
#     vector_store_id= 'vs_iuWC5kHGiffRSzSfa0eMaMxs'
# )



## 어시스턴트 업데이트
assistant = client.beta.assistants.update(
    # assistant_id= ass_id,
    name= 'Test ChatBot🤖',
    instructions = instructions,
    model ='gpt-4o-mini',
    tools =  [{'type': 'file_search'}],
    # tool_resources={'file_search': {'vector_store_ids':[vector_store.id]}},
    temperature=0.86,
)


assistant_info = client.beta.assistants.retrieve(assistant_id=ass_id)
print(f"[현재 어시스턴트 정보]\n{assistant_info}")




###############################################################


# ### 백터스토어 생성및 파일 임베딩 업로드 ####
# vector_store = client.beta.vector_stores.create(
#     name = '[ Nocoding AI ] Chatbot',
# )

# # #업로드할 파일들의 경로를 지정
# files_to_uploaded = [
#     '/Users/ainomis_dev/Desktop/ainomis/chatbot-nocoding/.docs/nocodingAI_models.md',
#     '/Users/ainomis_dev/Desktop/ainomis/chatbot-nocoding/.docs/preparing_models.md',
# ]

# file_streams = [open(path, 'rb') for path in files_to_uploaded]

# # 파일 업로드 및 백터 스토어에 추가
# file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
#     vector_store_id=vector_store.id, files = file_streams
# )


###############################################################


# #### 어시스턴트 리스트 검색 ####
# assistant_list = client.beta.assistants.list()

# for assistant in assistant_list:
#     print(f"[Assistant Name]: {assistant.name}, [Assistant ID] : {assistant.id}")


###############################################################


## vectorstore 삭제 ###
# vector_store = client.beta.vector_stores.delete(
#     vector_store_id='vs_iuSR8xFYdZML64ycdt8TC6BW'
# )


###############################################################


# ## 벡터스토어 리스트 검색 ###
# vector_store_list = client.beta.vector_stores.list()

# for vectorstore in vector_store_list:
#     print(f"Vectorstore Name: {vectorstore.name}, Vectorstore ID: {vectorstore.id}")

################################################################

# # ## 백터스토어 아이디 안 파일 리스트 ####
# vector_store_files = client.beta.vector_stores.retrieve(
#     vector_store_id='vs_0dJoKkouQ6Qa7HbczRnwC1VG',
# )
# file_ids = vector_store_files.file_counts

# print('백터스토어에 저장된 파일 목록 : ')
# for file_id in file_ids:
#     print(file_id)