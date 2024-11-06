import streamlit as st


st.title("메모를 저장하세요 ")
# 메모 저장 공간 초기화 (세션에 없으면 빈 리스트로 설정)
if "save_memos" not in st.session_state:
    st.session_state["save_memos"] = []

# 메모가 있으면 출력
if st.session_state["save_memos"]:
    for idx, memo in enumerate(st.session_state["save_memos"], 1):
        st.write(f"- {memo}")
else:
    st.write("챗봇과 대화 후 유용한 메시지를 저장해보세요.")