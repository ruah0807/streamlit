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
    
    save_memo = st.Page(
        "page/save_memo.py",
        title = "Assistant Memo",
        icon="🔖"
    ) 

    with st.sidebar :
        pages = {
            "Main" : [main],
            "Save DB":[
                save_db,
                # assistant,
                # save_memo
            ]
        }

    
    return pages
  