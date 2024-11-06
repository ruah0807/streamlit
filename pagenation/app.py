import streamlit as st
from sidebar import render_sidebar

def main():

    sidebar = render_sidebar()

    pg = st.navigation(sidebar)

    # 선택한 페이지를 실행
    pg.run()  # 선택된 페이지를 실행

if __name__ == '__main__':
    main()

