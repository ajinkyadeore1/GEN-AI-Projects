'''from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv("Google_API_Key"))

## Function to load Gemini Pro Model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response= chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

## Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:",key="input")
submit=st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    # add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
st.subheader("The Chat History is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")'''

from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import json  # For saving chat history

# Load environment variables
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("Google_API_Key"))

# Function to load Gemini Pro Model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    full_response = "".join([chunk.text for chunk in response])
    return full_response

# Function to save chat history to a file
def save_chat_history(history, filename="chat_history.json"):
    with open(filename, "w") as file:
        json.dump(history, file)

# Function to load chat history from a file
def load_chat_history(filename="chat_history.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return []

# Initialize the app
st.set_page_config(page_title="Q&A Demo", layout="wide")
st.header("Gemini LLM Application")

# Load chat history from file
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = load_chat_history()

# Sidebar for options
with st.sidebar:
    st.title("Options")
    if st.button("Clear Chat History"):
        st.session_state['chat_history'] = []
        save_chat_history([])
        st.success("Chat history cleared!")

# Chat input and response
with st.container():
    input_text = st.text_input("Ask your question:", key="input")
    if st.button("Submit"):
        if input_text:
            response = get_gemini_response(input_text)
            # Add user query and bot response to history
            st.session_state['chat_history'].append(("You", input_text))
            st.session_state['chat_history'].append(("Bot", response))
            save_chat_history(st.session_state['chat_history'])  # Save to file
            st.success("Response received!")

# Display chat history in a better format
st.subheader("Chat History")
for role, text in st.session_state['chat_history']:
    if role == "You":
        st.chat_message("user").write(text)
    elif role == "Bot":
        st.chat_message("assistant").write(text)