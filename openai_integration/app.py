import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Gen AI Chatbot Workshop", page_icon="🤖", layout="centered")

st.title("🤖 Gen AI Chatbot")
st.caption("A training workshop demo powered by OpenAI")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with st.sidebar:
    st.header("Settings")
    
    if st.button("Clear Chat History", type="secondary"):
        st.session_state.messages = []
        st.rerun()


def get_ai_response(messages: list) -> str:
    """
    Generate a response from OpenAI API.
    
    Args:
        messages: List of message dictionaries with 'role' and 'content' keys
    
    Returns:
        The assistant's response as a string
    
    TODO: Implement the OpenAI API call here
    Hints:
        - Use client.chat.completions.create()
        - Choose a model (e.g., 'gpt-4o-mini')
        - Extract the response from choices[0].message.content
    """
    pass


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                assistant_message = get_ai_response(
                    messages=st.session_state.messages
                )
            
            if assistant_message:
                st.markdown(assistant_message)
                st.session_state.messages.append({"role": "assistant", "content": assistant_message})
            else:
                st.warning("No response received. Implement the get_ai_response() function.")
            
        except Exception as e:
            st.error(f"Error: {str(e)}")

with st.expander("ℹ️ About this Demo"):
    st.markdown("""
    **Workshop Exercise:**
    
    Implement the `get_ai_response()` function to connect to OpenAI.
    
    **Steps:**
    1. Call `client.chat.completions.create()` with model and messages
    2. Return the assistant's message content
    """)