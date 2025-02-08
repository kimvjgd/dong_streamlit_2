# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import OpenAI, ChatOpenAI
import streamlit as st




chat_model = ChatOpenAI()

# 주제
st.title("인공지능 시인 욜로!~")
content = st.text_input("시의 주제를 제시해주세요.")

if st.button("시 작성 요청하기"):
    with st.spinner("wait for it...."):
        result = chat_model.invoke(f"{content}에 대한 시를 한국말로 써줘")
        print(result.content)

        st.write(result.content)




