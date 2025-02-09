from dotenv import load_dotenv
import os
from langchain_openai import OpenAI, ChatOpenAI
import streamlit as st

# .env 파일 로드
load_dotenv()

# OpenAI API 키 설정
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("⚠️ OpenAI API 키가 설정되지 않았습니다. .env 파일을 확인하세요.")

chat_model = ChatOpenAI(openai_api_key=api_key)

# 주제
st.title("인공지능 시인 욜로!~")
content = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 작성 요청하기"):
    with st.spinner("wait for it...."):
        result = chat_model.invoke(f"{content}에 대한 시를 한국말로 써줘")
        print(result.content)
        st.write(result.content)
