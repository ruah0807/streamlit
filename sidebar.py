import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.header("연도 선택")
        if st.button("main"):
            st.session_state.current_page = "main"
        if st.button("2021"):
            st.session_state.current_page = "2021"
        if st.button("2022"):
            st.session_state.current_page = "2022"
        if st.button("2023"):
            st.session_state.current_page = "2023"
        if st.button("2024"):
            st.session_state.current_page = "2024"

    
