# pip install -r requirements.txt

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os 

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.0-pro-latest')
# chat = model.start_chat(hisrtory=[])
chat = model.start_chat(history=[])


def get_response(question):
    response = chat.send_message(question, stream=True)
    return response


def main():
    st.set_page_config("Normal QnA Bot with Chat History", "::robot::")
    st.title("Conversational Bot with Chat History")

    # Function for chat history and intializing session state 
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    input = st.text_input("Input:", key="input")
    submit = st.button("Get Response")

    if submit and input:
        response = get_response(input)
        st.session_state['chat_history'].append(("User Question: ", input))
        st.subheader("The Response is")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot Response: ", chunk.text))
        
        st.success("Done!")

    st.subheader("The Chat History is")
        
    for role, text in st.session_state['chat_history']:
        st.write(f"{role} : {text}")
        

if __name__ == '__main__':
    main()

# Refrence: https://pypi.org/project/google-generativeai/, https://github.com/google-gemini/generative-ai-python

# In this code response object returned by chat.send_message is being processed in chunks, and each chunk is being appended to the chat 
# history as a separate entry. Thus for each chunk "Bot Response: " appears in the chat history. 

# To resolve this, we can collect all the chunks into a single response string before appending it to the chat history. Implement:
    # Collect the response chunks: Aggregate the chunks into a single string before displaying them and storing them in the session state.
    # Append the aggregated response: Add the entire response as one entry in the chat history.
    
    # Code Implemetation: 
    # def get_response(question):
    # response_chunks = chat.send_message(question, stream=True)
    # response_text = ''.join(chunk.text for chunk in response_chunks)
    # return response_text