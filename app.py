import streamlit as st
import chatgpt
chatbot = chatgpt.ChatGPT()
chatbot.set_language("english")
chatbot.set_modality("text")
user_input = st.text_input("Enter your message:")
response = chatbot.get_response(user_input)
st.write(f"Chatbot: {response}")

