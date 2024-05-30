from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as  genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#function to load gemini pro model and get responses
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

## Streamlit app

st.set_page_config(page_title='Question & Answer Demo')

st.header('Gemini LLM application ')

input = st.text_input('Input:',key='input')
submit = st.button('Ask your Question')

## When submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader('The response is')
    st.write(response)