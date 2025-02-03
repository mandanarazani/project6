import streamlit as st
# import requests
# from bs4 import BeautifulSoup
from groq import Groq
 
# Add images for branding
st.image("./assets/Untitled17_20250113001924.png", width=400)
st.sidebar.image("./assets/reshot-icon-flowers-in-the-branch-QXUYA35D8W.svg", width=180)
 
# Sidebar navigation
page = st.sidebar.radio("", ["About", "Shop", "ChatBot"])
 
if page == "About":
    st.title("SAKURA Online Shop")
    st.write("Welcome to our world!")


        
elif page == "ChatBot":
    st.title("ChatBot Page")
    st.write("Chat with the bot here!")



    # Initialize Groq client
    client = Groq(api_key="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")

    # Default model - update this with the correct model name
    model = "gemma2-9b-it"

    # Initialize conversation history if not in session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    # Display the chat history
    st.title("ChatBot Page")
    st.write("Chat with the bot here!")

    # Display existing chat messages
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Handle user input
    if prompt := st.chat_input("Ask something..."):
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)  # Display user message

        # Send the conversation history to the Groq API
        conversation = [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state["messages"]]

        try:
            # Call Groq API for completion
            with st.spinner('Generating response...'):
                completion = client.chat.completions.create(
                    model=model,
                    messages=conversation
                )
                assistant_response = completion.choices[0].message.content

            # Add assistant response to session state
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            st.chat_message("assistant").write(assistant_response)  # Display assistant message

        except Exception as e:
            # Handle error if model is not found or other issues
            st.error(f"Error: {e}")
            st.write("Please check the model name or your access permissions.")

