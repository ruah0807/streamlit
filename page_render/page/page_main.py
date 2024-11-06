import streamlit as st
from PIL import Image

    # 로고 이미지 추가
    # logo = Image.open("/Users/ainomis_dev/Desktop/ainomis/streamlit/_img/k-water_logo.png")

    # st.image(logo, width=300)

    # 전체페이지 구성

st.title(":blue[K-water] 수자원공사 챗봇")

st.write("""
K-water의 30년 이상 축적된 해외사업 정보와 사내 전문 정보 시스템에 효율적으로 접근할 수 있는 AI 챗봇입니다. \n
연도별로 정리된 카테고리별 데이터를 활용하여, 사용자가 원하는 연도와 주제에 맞는 문서를 검색하고 신속하게 답변합니다.\n
    """)
st.code("""
[ 이용 방법 ]
1. 질문 입력: 한국어로 질문을 입력하세요. 예를 들어 "2021년 (특정)해외사업 보고서 내용"과 같이 입력하면, 챗봇이 해당 연도의 관련 문서를 우선적으로 검색합니다.
2. 결과 확인: 챗봇이 선택한 연도의 자료에서 가장 적합한 답변을 찾아 제공해줍니다. 추가적으로 더 많은 정보가 필요하면, 추가 질문을 통해 챗봇과 상호작용할 수 있습니다.

이 챗봇은 K-water의 방대한 연도별 데이터를 체계적으로 관리하며, 사용자에게 필요한 정보를 빠르게 제공할 수 있도록 설계되어 있어 업무의 효율성을 높이는 데 도움이 됩니다.
""")
    # # 메모 저장 공간 초기화 (세션에 없으면 빈 리스트로 설정)
    # if "save_memos" not in st.session_state:
    #     st.session_state["save_memos"] = []

    # # 메모가 있으면 출력
    # if st.session_state["save_memos"]:
    #     for idx, memo in enumerate(st.session_state["save_memos"], 1):
    #         st.write(f"- {memo}")
    # else:
    #     st.write("챗봇과 대화 후 유용한 메시지를 저장해보세요.")