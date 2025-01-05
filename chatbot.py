import streamlit as st

# Function to simulate a simple chatbot response
def get_bot_response(user_input):
    # This is a simple example where bot responds to the user input
    # You can replace this with more sophisticated AI models or APIs
    if user_input:
        return "You said: " + user_input
    else:
        return "Hello! How can I help you today?"

# Setting up the chatbot interface
st.title("Chatbot Interface")
st.subheader("Talk to me!")

# Chat history storage
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Display chat history
for message in st.session_state['history']:
    st.chat_message(message['role']).markdown(message['content'])

# User input area
user_input = st.text_input("You:", key="input")

# Send button functionality
if user_input:
    # Add user message to chat history
    st.session_state['history'].append({"role": "user", "content": user_input})
    
    # Get bot response
    bot_response = get_bot_response(user_input)
    
    # Add bot message to chat history
    st.session_state['history'].append({"role": "bot", "content": bot_response})

    # Clear input field
    st.text_input("You:", "", key="input", placeholder="Enter your message")
