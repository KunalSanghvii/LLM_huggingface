import streamlit as st
from main import get_bot_response

st.set_page_config(page_title="Customer Support Chatbot", page_icon="🤖")
st.title("🤖 Customer Support Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask your question: ")

if user_input:
    with st.spinner("Thinking.."):
        response = get_bot_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", user_input))

for sender, msg in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑‍💼 You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")