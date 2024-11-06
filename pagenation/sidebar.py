import streamlit as st

def render_sidebar():
    
    main = st.Page(
        "page/page_main.py",
        title = "K-Water 챗봇",
        icon = "🤖",
        default=True
    )

    save_db = st.Page(
        "page/save_db.py",
        title = "Upload DB",
        icon="📂"
    ) 

    assistant = st.Page(
        "page/assistant.py",
        title = "OpenAI Assistant",
        icon="🪩"
    ) 

    with st.sidebar :
        pages = {
            "Main" : [main],
            "Others":[
                save_db,
                assistant,
            ]
        }

    

    
    return pages
  