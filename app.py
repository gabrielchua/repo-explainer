"""
app.py
"""
import os
import time

import google.generativeai as genai
import streamlit as st

from utils import retrieve_github_repo_info

GITHUB_TOKEN = os.getenv("GH_API_KEY")

if "repo" not in st.session_state:
    st.session_state.repo = None

def generate_response(prompt):
    stream = st.session_state.chat_model.send_message(prompt, stream=True)
    for chunk in stream:
        for char in chunk.text:
            time.sleep(0.01)
            yield char

##############
st.set_page_config(page_title="Repo Explainer",
                   page_icon="📦")

st.title("📦 Repo Explainer")

repo_box = st.empty()
github_url = repo_box.text_input("Enter a GitHub URL:")

if "github.com" not in github_url:
    st.stop()

if st.session_state.repo is None:
    with st.spinner("Fetching repository information..."):
        st.session_state["repo"] = retrieve_github_repo_info(github_url, token=GITHUB_TOKEN)

    model = genai.GenerativeModel("gemini-1.5-pro-latest",
                                  system_instruction="You are a coding expert who analyses GitHub repos. "
                                                    "When replying, be succinct and polite. Avoid markdown title headers. "
                                                    "When citing files or variables, use backticks for markdown formatting."
                                                    f"Base your answers on this repo: {st.session_state.repo}")


    st.session_state.chat_model = model.start_chat(history=[])

if st.session_state["repo"] is not None:
    repo_box.empty()

    # Store LLM generated responses
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User-provided prompt
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt) 
                st.write_stream(response) 
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)
