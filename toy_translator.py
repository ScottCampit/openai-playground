import os
import openai
import streamlit as st

model_engine = "text-davinci-002"
openai.api_key = os.environ["OPENAI_API_KEY"]

def translate(user_prompt, target_language):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt="Translate from English to " + target_language + ": " + user_prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    return message

st.title("Language Translation App")
input_text = st.text_area(label="Enter text to translate:")

# Add buttons for selecting the target language
target_language = st.radio(
    "Select target language:",
    ("Spanish", "French", "Mandarin")
)

# Translate the text and display the result
if input_text:
    translated_text = translate(input_text, target_language)
    st.success(translated_text)