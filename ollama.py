from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
import time,json

# spaCy 모델 로드
llm = Ollama(model = "gemma2:9b")



chat_template = ChatPromptTemplate.from_messages(
[
    ("system", """
    질문에서 중요한 키워드를 골라주세요 응답형식은 아래와 같습니다:
     {{
        "year": "(연도가 있다면 입력 )",
        "keywords" : [
        "(연도 외의 키워드(지명, 이름 등)를 중요도 순위대로 입력)",
        ]
     }}
"""),
("human", "{user_input}")
]
)
message = chat_template.format_messages(
    user_input = "2021년 k-water에서 홍길동님을 위해 인도 스마랑시에서 준비한 행사는 무엇인가요?"
)

#  텍스트에서 JSON 부분만 추출하여 반환하는 함수
def extract_json_from_text(text):
    try:
        # 응답 텍스트에서 JSON 부분을 찾기
        start = text.find('{')
        end = text.rfind('}') + 1
        # JSON 형식의 부분만 추출
        if start != -1 and end != -1:
            json_str = text[start:end]  # 중괄호 안의 내용만 추출
            return json.loads(json_str)  # JSON 파싱 시도
        else:
            print("JSON 형식의 데이터를 찾을 수 없습니다.")
            return None
    except json.JSONDecodeError as e:
        print(f"JSON 파싱 실패: {e}")
        return None
    

def print_parsed_result(response):
    data = extract_json_from_text(response)
    year = data.get("year")
    keywords = data.get("keywords")
    result = {"year": year, "keywords": keywords}
    return result
    

def execute(message):
    start_time = time.time()
    chain = chat_template | llm
    response = chain.invoke(message)
    result = print_parsed_result(response)
    end_time = time.time()
    total_duration = f"전체 처리시간 : {int((end_time-start_time)//60)}분 {(end_time-start_time)%60:.2f}초"

    result = {"result": result, "total_duration": total_duration}    
    return print(result)

execute(message)
# response = chain.stream(message)
# for res in response :
#     print(res, end = "", flush=True)
    
