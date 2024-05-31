# Ensure all required packages are installed
# pip install -r requirements.txt

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Configure the Generative AI model with the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set GOOGLE_API_KEY in your .env file.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.0-pro-latest')

# Start a chat session with an empty history
chat = model.start_chat(history=[])

# Function to get the response from the Generative AI model
def get_response(question):
    response_chunks = chat.send_message(question, stream=True)
    response_text = ''.join(chunk.text for chunk in response_chunks)
    return response_text

def main():
    st.set_page_config(page_title="Normal QnA Bot with Chat History", page_icon="::robot::")
    st.title("Conversational Bot with Chat History")

    # Initialize chat history in session state
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    user_input = st.text_input("Input:", key="input")
    submit = st.button("Get Response")

    if submit and user_input:
        with st.spinner('Response in Progress...'):
            response = get_response(user_input)
            st.session_state['chat_history'].append(("User Question:", user_input))
            st.session_state['chat_history'].append(("Bot Response:", response))

        st.subheader("The Response is")
        st.write(response)
        st.success("Done!")

    st.subheader("The Chat History is")
    for role, text in st.session_state['chat_history']:
        st.write(f"{role} {text}")

if __name__ == '__main__':
    main()

# Reference: https://pypi.org/project/google-generativeai/, https://github.com/google-gemini/generative-ai-python