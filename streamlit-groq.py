from groq import Groq
from dotenv import load_dotenv, find_dotenv
import streamlit as st
_ = load_dotenv(find_dotenv())
st.title('Small app by XC😎')
client = Groq(
    api_key="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",
)
def generate_text(input_text):
    response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI Assistant. You explain ever \
            topic the user asks as if you are explaining it to a 5 year old"
        },
        {
            "role": "user",
            "content": input_text,
        }
    ],
    model="mixtral-8x7b-32768",
    )
    st.info(response.choices[0].message.content)

with st.form('my_form'):
    text = st.text_area('Enter text:', '')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_text(text)