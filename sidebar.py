import streamlit as st


def render_sidebar():
    with st.sidebar:

        main = st.Page(
            "page/page_main.py",
            title = "Main Page",
            icon = ":material/home:"
        )

        page_2021 = st.Page(
            "page/page_2021.py",
            title = "2021",
        ) 

        page_2022 = st.Page(
            "page/page_2022.py",
            title = "2022",
        ) 

        page_2023 = st.Page(
            "page/page_2023.py",
            title = "2023",
        ) 

        page_2024 = st.Page(
            "page/page_2024.py",
            title = "2024",
        ) 

        pages = {
            "Home" : [main],
            "K-water Informations":[
                page_2021,
                page_2022,
                page_2023,
                page_2024
            ]
        }
    
    return pages
    

        # if main:
        #     st.session_state.current_page = "main"
        # if st.button("2021"):
        #     st.session_state.current_page = "2021"
        # if st.button("2022"):
        #     st.session_state.current_page = "2022"
        # if st.button("2023"):
        #     st.session_state.current_page = "2023"
        # if st.button("2024"):
        #     st.session_state.current_page = "2024"

    

