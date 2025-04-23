
import openai
import streamlit as st

# Set up your OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initialize the chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to get response from OpenAI
def get_openai_response(user_input):
    # Append the user input to the chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Call OpenAI's API using the new method
    try:
        response = openai.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=st.session_state.chat_history,
            temperature=0.7  # Adjust this as needed
        )
        answer = response['choices'][0]['message']['content']
        # Append the assistant's reply to the chat history
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        return answer

    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("Lev Vygotsky Chatbot")
user_name = st.text_input("What's your name?")

if user_name:
    user_input = st.text_input(f"Hello, {user_name}! Ask a question related to Vygotsky's work:")
    
    if user_input:
        # Get OpenAI response
        answer = get_openai_response(user_input)
        st.write(answer)
else:
    st.write("Please enter your name to start the conversation.")
