import streamlit as st
from groq import Groq

# --- Set up Groq API ---
GROQ_API_KEY = "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"  # Replace with your actual key
client = Groq(api_key=GROQ_API_KEY)

# --- Streamlit App Setup ---
st.set_page_config(page_title="Groq Chatbot", layout="centered")
st.title("🤖 Groq Web Chatbot")
st.write("Ask me anything! Powered by LLaMA 3 via GroqCloud")

# --- Session State to store chat ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display old messages ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Input box ---
user_input = st.chat_input("Type your message here...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call Groq LLM
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=st.session_state.messages
    )
    bot_reply = response.choices[0].message.content

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
