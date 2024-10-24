import streamlit as st
import pandas as pd
from io import StringIO

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
    

def handle_file_upload():
    with st.sidebar:
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None :
            bytes_data = uploaded_file.getvalue()
            st.write(bytes_data)

            # to convert to a string based IO :
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            st.write(stringio)

            # Can be used wherever a "file-like" object is accepted:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)

    return uploaded_file


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

    

