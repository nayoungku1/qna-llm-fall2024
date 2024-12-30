import streamlit as st
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI

st.title("💬 창조와 진화 LLM")


# OpenAI API Key 설정
with st.sidebar:
    # secrets.toml에서 기본 키 불러오기 (없는 경우 빈 문자열로 설정)
    default_api_key = st.secrets.get("openai_api_key", "")
    
    # 사이드바에서 OpenAI API Key 입력 받기 (기본값 설정)
    openai_api_key = st.text_input(
        "OpenAI API Key",
        value=default_api_key,
        type="password",  # 입력 값을 숨김
    )

    # 키가 입력되었는지 확인하고 표시 (디버깅 또는 확인용, 실제 배포 시 제거 가능)
    if openai_api_key:
        st.write("API Key is set.")
    else:
        st.warning("Please enter your OpenAI API Key.")

# 노아의 홍수는 진짜 있었던 일인가요?
if prompt := st.chat_input("무엇이 궁금하세요?"):
    with st.chat_message("user"):
        st.markdown(prompt)


if openai_api_key:
    model = ChatOpenAI(api_key=openai_api_key, model_name = "gpt-4o-mini", temperature = 0)
    embedding_model = OpenAIEmbeddings(
        api_key=openai_api_key, model = "text-embedding-3-large"
    )
    
    db = Chroma(
        persist_directory="./rag/chroma_db", embedding_function=embedding_model
    )
    
    retriever = db.as_retriever(
        search_type="mmr", search_kwargs={"k": 1, "fetch_k": 5, "lambda_mult":0.8}
    )

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content= "당신은 지적설계를 지지하는 과학자입니다."
        ),
        HumanMessagePromptTemplate.from_template(
            """
            {question}
            아래의 문맥에 기반하여 답하여 주세요.
            {context}

            문맥에서 언급되었다는 투의 말을 생략하고 응답을 제공해주세요.
            """
        )
    ]
)

if not openai_api_key and prompt:
    with st.chat_message("assistant"):
        st.write("OpenAI API Key를 입력해주세요.")

if openai_api_key and prompt:
    context = retriever.invoke(prompt)

    message= chat_template.format_messages(
        question=prompt,
        context=context[0].page_content
    )

    def stream_responses(stream):
        for chunk in stream:
            yield chunk.content 

    with st.chat_message("assistant"):
        stream = model.stream(message)  # Get the stream from the model
        st.write_stream(stream_responses(stream))
        