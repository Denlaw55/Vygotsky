import streamlit as st
import openai

# Set up your OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initialize the chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "system", "content": (
        "You are Lev Vygotsky, a Russian psychologist. You only answer questions related "
        "to your theories, such as sociocultural learning, the Zone of Proximal Development (ZPD), "
        "scaffolding, and child development. All answers must cite a peer-reviewed reference. If none "
        "can be found, offer suggestions for how to search academic library databases.")}]

# Function to get response from OpenAI
def get_openai_response(user_input):
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Or use "gpt-4" if available
            messages=st.session_state.chat_history,
            temperature=0.7
        )
        answer = response.choices[0].message.content
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        return answer
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("Lev Vygotsky Chatbot")

user_name = st.text_input("What's your name?")

if user_name:
    user_input = st.text_input(f"Hello {user_name}, ask a question related to Lev Vygotsky's theories:")

    if user_input:
        response = get_openai_response(user_input)
        st.write(response)
else:
    st.write("Please enter your name to start.")
