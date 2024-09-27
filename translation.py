import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gpt

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Translate with Gemini",
    page_icon=":globe_with_meridians:",  # Favicon emoji
    layout="wide",
)

# Get API Key from .env file
API_KEY = os.getenv("API_KEY")  # Ensure you have the API_KEY in your .env

# Set up Google Gemini AI model
gpt.configure(api_key=API_KEY)
model = gpt.GenerativeModel('gemini-pro')

# Streamlit app UI
st.title("🌍 Translate with Gemini")
source_text = st.text_area("Enter text to translate:")
target_language = st.selectbox("Select target language:", ["en", "Hindi", "Telgu", "Tamil "])  # Add more languages as needed

if st.button("Translate"):
    if source_text:
        # Generate translation using the Gemini model
        try:
            translation_response = model.generate_content(f"Translate the following text to {target_language}: {source_text}")
            translated_text = translation_response.parts[0].text
            
            # Display the translated text
            st.subheader("Translated Text:")
            st.write(translated_text)
        except Exception as e:
            st.error(f"Error in translation: {e}")
    else:
        st.warning("Please enter text to translate.")
