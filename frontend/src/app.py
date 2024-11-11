import streamlit as st
from api import fetch_messages, send_message

st.title("ChatGPT 4.0 Mini Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

# 최근 메시지 가져오기
st.session_state.messages = fetch_messages()

# 채팅 히스토리 표시
for message in reversed(st.session_state.messages):
    with st.chat_message("user"):
        st.write(message["content"])
    with st.chat_message("assistant"):
        st.write(message["response"])

# 사용자 입력
user_input = st.text_input("메시지를 입력하세요")

if user_input:
    # API 요청
    new_message = send_message(user_input)
    if new_message:
        st.session_state.messages.insert(0, new_message)
        
        # 새 메시지 표시
        with st.chat_message("user"):
            st.write(new_message["content"])
        with st.chat_message("assistant"):
            st.write(new_message["response"])