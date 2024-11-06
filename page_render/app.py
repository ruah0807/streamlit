import streamlit as st
from sidebar import render_sidebar
# from page.page_main import main

def main():

    sidebar = render_sidebar()

    pg = st.navigation(sidebar)

    # 선택한 페이지를 실행
    pg.run()  # 선택된 페이지를 실행

if __name__ == '__main__':
    main()




#현재페이지 상태 초기화
# if 'current_page' not in st.session_state:
#     st.session_state['current_page'] = "Home"

# selected_page = st.session_state["current_page"]



# # 현재 페이지에 따라 콘텐츠 표시
# if st.session_state.current_page =='main':
#     page_main.page_main()
# elif st.session_state.current_page =='2021':
#     page_2021.page_2021()
# elif st.session_state.current_page =='2022':
#     save_db.()
# elif st.session_state.current_page =='2023':
#     page_2023.page_2023()
# elif st.session_state.current_page =='202':
#     page_2024.page_2024()