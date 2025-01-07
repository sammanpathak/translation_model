import streamlit as st
from transformers import pipeline

# Initialize translation pipeline with your Hugging Face model
model_name = "samman100/Translation_model_lol"
translator = pipeline("translation_xx_to_yy", model=model_name)

# Set the title and description of the app
st.set_page_config(page_title="Nepali to English Translator",
                   page_icon="🇳🇵", layout="centered")
st.title("Nepali to English Translation")
st.markdown(
    "Translate Nepali sentences into English using the latest machine translation models.")

# Input for Nepali text
st.subheader("Enter Nepali Text:")
user_input = st.text_area("Type Nepali sentence here:",
                          height=150, placeholder="e.g. तपाईंलाई कस्तो छ?")

# Translation button
if st.button("Translate"):
    if user_input:
        with st.spinner("Translating..."):
            translation = translator(user_input)
            translated_text = translation[0]['translation_text']
            st.markdown(f"### Translation:")
            st.write(translated_text)
    else:
        st.error("Please enter a Nepali sentence to translate.")

# Footer with additional information
st.markdown("""
---
Made with ❤️ using Hugging Face Transformers and Streamlit.
""", unsafe_allow_html=True)
