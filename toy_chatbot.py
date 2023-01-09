import os
import openai
import streamlit as st

openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_response(prompt:str, temperature:float=0.5, max_tokens:int=1500, engine='davinci'):
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0.3
    )
    generated_text = response["choices"][0]["text"]
    return generated_text

st.title("Chatbot Assistant")
prompt = st.text_input(label="Enter your message: ")
if prompt:
  response = generate_response(prompt)
  st.write("Chatbot:", response)