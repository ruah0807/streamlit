import streamlit as st
import pandas as pd
from io import BytesIO
import os

def render_sidebar():
    
    main = st.Page(
        "page/page_main.py",
        title = "Main Page",
        icon = "🏠",
        default=True
    )

    save_db = st.Page(
        "page/save_db.py",
        title = "Upload DB",
        icon="📂"
    ) 

    page_2021 = st.Page(
        "page/page_2021.py",
        title = "2021",
    ) 

    page_2023 = st.Page(
        "page/page_2023.py",
        title = "2023",
    ) 

    page_2024 = st.Page(
        "page/page_2024.py",
        title = "2024",
    ) 

    with st.sidebar :
        pages = {
            "Home" : [main],
            "Upload K-water Informations":[
                save_db,
                page_2021,
                page_2023,
                page_2024
            ]
        }

    

    
    return pages
  