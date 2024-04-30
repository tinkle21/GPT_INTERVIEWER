import streamlit as st
import time
from streamlit_lottie import st_lottie
import json
from aiinterview import chatConversation


def query(OPENAI_API_KEY):
    if "jobdescription" not in st.session_state:
        st.session_state.jobdescription = None
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "open_api_key" not in st.session_state:
        st.session_state.open_api_key = None
    if "count" not in st.session_state:
        st.session_state.count = 0
    if "display_analytics" not in st.session_state:
        st.session_state.display_analytics = False
    jd = st.text_area(
        "Please enter the job description here (If you don't have one, enter keywords, such as PostgreSQL or Python instead): ")
    st.session_state.jobdescription = jd
    if len(st.session_state.messages) >= 16:
        if st.button("Submit Interview!"):
            st.session_state.display_analytics = True
            st.switch_page("pages/Feedback Analytics.py")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    jobdescription_and_skills = {"job_description_is": jd}
    if st.session_state.jobdescription:
        if st.session_state.count == 0:
            st.write("Type hi below to start...")
            st.session_state.count = 1

        if answer := st.chat_input("write your answer here..."):
            st.session_state.messages.append(
                {"role": "user", "content": answer})
            with st.chat_message("user"):
                st.markdown(answer)
            with st.spinner("thinking..."):
                response = chatConversation(
                    answer, jobdescription_and_skills, OPENAI_API_KEY)
            if response:
                with st.chat_message(name="assistant"):
                    message_placeholder = st.empty()
                    full_response = ""
                    for chunk in response['text'].split():
                        full_response += chunk + " "
                        time.sleep(0.05)
                        message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
                st.session_state.messages.append(
                    {"role": "assistant", "content": full_response})
            else:
                st.warning("Invalid API key")
                st.session_state.messages = []


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


st_lottie(load_lottiefile("welcome.json"), speed=1,
          reverse=False, loop=True, quality="high", height=300)
with st.sidebar:
    OPENAI_API_KEY = st.text_input(placeholder="OPENAI API KEY", label="OPENAI API KEY",
                                   type="password", key="OPENAI_API_KEY", label_visibility="collapsed")

if OPENAI_API_KEY:
    st.session_state.open_api_key = OPENAI_API_KEY
    query(OPENAI_API_KEY)
