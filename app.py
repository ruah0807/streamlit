import streamlit as st
from sidebar import render_sidebar

def main():
    # 전체페이지 구성
    st.set_page_config(
        page_title="Text Generator by Kwater",
        page_icon=":information_source:",
        initial_sidebar_state="collapsed",)  # 사이드바를 기본적으로 숨김 상태로 설정


    sidebar = render_sidebar()

    pg = st.navigation(sidebar)

    # 선택한 페이지를 실행
    pg.run()  # 선택된 페이지를 실행

if __name__ == '__main__':
    main()

