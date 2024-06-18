from groq import Groq
from dotenv import load_dotenv, find_dotenv
import streamlit as st
_ = load_dotenv(find_dotenv())
st.title('Chat with Groq!😎')
client = Groq(
    api_key="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",
)
def generate_text(input_text):
    response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI Assistant. You explain ever \
            topic the user asks. If user asks you in Chinese, you need use Chinese to answer."
        },
        {
            "role": "user",
            "content": input_text,
        }
    ],
    model="mixtral-8x7b-32768",
    )
    st.info(response.choices[0].message.content)

if 'messages' not in st.session_state:
    st.session_state.messages = []
messages = st.container(height=300)

if prompt := st.chat_input("Say something"):
    st.session_state.messages.append({"role": "user", "text": prompt})
    answer = generate_text(prompt)
    if answer is not None:
        st.session_state.messages.append({"role": "assistant", "text":
    answer})
        
for message in st.session_state.messages:
    if message["role"] == "user":
        messages.chat_message("user").write(message["text"])
    elif message["role"] == "assistant":
        messages.chat_message("assistant").write(message["text"]) 
