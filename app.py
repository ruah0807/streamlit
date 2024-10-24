import streamlit as st
from sidebar import render_sidebar, handle_file_upload
from page import page_2021, page_2022, page_2023, page_2024, page_main


#사이드바 랜더링
sidebar =render_sidebar()

handle_file_upload()

pg = st.navigation(sidebar)

pg.run()




#현재페이지 상태 초기화
# if 'current_page' not in st.session_state:
#     st.session_state['current_page'] = "Home"

# selected_page = st.session_state["current_page"]



# 현재 페이지에 따라 콘텐츠 표시
# if st.session_state.current_page =='main':
#     page_main.page_main()
# elif st.session_state.current_page =='2021':
#     page_2021.page_2021()
# elif st.session_state.current_page =='2022':
#     page_2022.page_2022()
# elif st.session_state.current_page =='2023':
#     page_2023.page_2023()
# elif st.session_state.current_page =='202':
#     page_2024.page_2024()