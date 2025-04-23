
import streamlit as st
import openai
import os

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Chat with Lev Vygotsky", layout="centered")

st.title("Chat with Lev Vygotsky")

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if not st.session_state.user_name:
    name = st.text_input("Before we begin, what is your name?")
    if name:
        st.session_state.user_name = name
        st.success(f"Welcome, {name}. Ask me anything related to my work or associated research.")
    st.stop()

st.markdown(f"Hello, **{st.session_state.user_name}**. You may ask about my theories, or ideas connected to my research.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": (
            "You are Lev Vygotsky, a Soviet psychologist and philosopher. Speak in an intellectual but accessible tone. "
            "Only respond to questions related to your own work or topics strongly associated with your theories "
            "(such as cognitive development, sociocultural learning, the Zone of Proximal Development, and scaffolding). "
            "Always include a peer-reviewed academic reference in your response. If you cannot find one, explain how the user "
            "might search for scholarly sources in an academic library database."
        )}
    ]

user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.chat_history
    )

    bot_reply = response['choices'][0]['message']['content']
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

for msg in st.session_state.chat_history[1:]:
    speaker = "Lev Vygotsky" if msg["role"] == "assistant" else st.session_state.user_name
    st.markdown(f"**{speaker}:** {msg['content']}")
