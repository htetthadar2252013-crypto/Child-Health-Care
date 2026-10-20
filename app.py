import streamlit as st

# Page Configuration
st.set_page_config(page_title="Child Health Assistant", page_icon="👶", layout="centered")

st.title("👶 Child Health Care Assistant")
st.markdown("Ask general health care and wellness questions for children.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
if prompt := st.chat_input("Ask a child health question..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response (Replace this with the Gemini API later!)
    with st.chat_message("assistant"):
        response = (
            f"You asked: **{prompt}**\n\n"
            "*(This is a sample reply. Later, we will connect this to an AI model like Gemini to give detailed health facts!)*\n\n"
            "> **Medical Disclaimer:** This app provides general educational facts only and does not replace professional medical advice."
        )
        st.markdown(response)
        
    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
