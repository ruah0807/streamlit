import streamlit as st
from openai import OpenAI
from init import api_key
import time

ass_id = 'asst_ifqkPUog6RMvmWD27YYGFS9M'

# if "openai_api_key" not in st.session_state:
#     st.session_state["openai_api_key"] = api_key

# openai_api_key = st.text_input("OpenAI API Key", 
#                                 key="chatbot_api_key", 
#                                 type="password", 
#                                 value=api_key )

client = OpenAI(api_key=api_key)


st.subheader(":blue[K-water] 수자원공사 챗봇")
st.write("2021년 수자원공사에 대해 무엇이든 물어보고 질문하세요")

##################################################################

# 세션 상태 초기화
if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = None

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "무엇을 도와드릴까요?"}]

if "save_memos" not in st.session_state:
    st.session_state["save_memos"] = []

if "show_save_button" not in st.session_state:
    st.session_state["show_save_button"] = False
    
if "thread_id" not in st.session_state:
        st.session_state["thread_id"] = None

##################################################################


#스레드 생성버튼(스레드가 없을 때만 활성화)
thread_btn = st.button('스레드 생성')
if thread_btn:
    if st.session_state["thread_id"] is None:
        thread = client.beta.threads.create()
        st.session_state["thread_id"] = thread.id
        st.info("스레드가 생성되었습니다. 대화를 시작할 수 있습니다.")
        # st.subheader(f"{thread_id}", divider="rainbow")
    else:   
        st.warning("스레드가 이미 존재합니다. 삭제 후 재생성 해주세요 ")


thread_del_btn = st.button("스레드 삭제")
if thread_del_btn:
    if st.session_state["thread_id"] is not None:
        thread_del = client.beta.threads.delete(st.session_state["thread_id"])
        st.session_state["thread_id" ]= None
        st.info(f"스레드가 삭제되었습니다. 대화를 시작하시려면 새로운 스래드를 생성해주세요.")
    else: 
        st.warning("삭제할 스래드가 존재하지 않습니다.")

##################################################################

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "무엇을 도와드릴까요?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    if st.session_state["thread_id"] is None:
        st.info("스레드를 먼저 생성해주세요.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    place_holder = st.chat_message("assistant")


    with place_holder: 
        with st.spinner("응답을 기다리는 중..."):
        
            response = client.beta.threads.messages.create(
                thread_id=st.session_state["thread_id"],
                role='user',
                content=prompt
            )
            # print(response)

            run = client.beta.threads.runs.create(
                thread_id= st.session_state["thread_id"],
                assistant_id=ass_id,
            )
            run_id = run.id

            while True:
                run = client.beta.threads.runs.retrieve(
                    thread_id=st.session_state["thread_id"],
                    run_id=run_id
                )
                if run.status == "completed":
                    break
                else:
                    time.sleep(2)
                print(run.status)

            thread_messages = client.beta.threads.messages.list(st.session_state["thread_id"])
            # print(thread_messages.data)

            msg = thread_messages.data[0].content[0].text.value
            print(msg)

            # 로딩메세지를 실제 응답으로 교체
            place_holder.write(msg)
            st.session_state.messages.append({"role": "assistant", "content": msg})  

            # 저장버튼의 상태를 관리하기 위한 세션 변수 초기화
            st.session_state["show_save_button"] = True

if st.session_state["show_save_button"]:
    # Save 버튼으로 마지막 assistant 메시지 저장
    if st.button("저장"):
        # 마지막 assistant 메시지 저장
        last_assistant_message = st.session_state["messages"][-1]["content"]
        st.session_state["save_memos"].append(last_assistant_message) 
        st.success("마지막 assistant의 메시지가 저장되었습니다.")
        # 저장 버튼을 숨김
        st.session_state["show_save_button"] = False

# #########################################################

# # 메모가 있으면 출력
# if st.session_state["save_memos"]:
#     st.subheader("저장 메모")
#     for idx, memo in enumerate(st.session_state["save_memos"], 1):
#         st.subheader(f"Memo {idx}")
#         st.write(memo)
# else:
#     st.write("저장된 메모가 없습니다.")