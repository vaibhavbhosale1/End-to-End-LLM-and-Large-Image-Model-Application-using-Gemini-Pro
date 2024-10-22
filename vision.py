from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as  genai
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#function to load gemini pro model and get responses
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input,image):
    if input != "" :
        
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text 

## Streamlit app

st.set_page_config(page_title='Gemini Image Demo')

st.header('Gemini application ')

input = st.text_input('Input Prompt:',key='input')

uploaded_file = st.file_uploader("Choose an image", type =['jpg', 'jpeg', 'png'])

image = ''

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploded Image', use_column_width=True)


submit = st.button('Tell me about your image')

## If submit clicked
if submit :
    

    response = get_gemini_response(input,image)
    st.header('The response is')
    st.write(response)