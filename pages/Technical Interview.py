import streamlit as st
import time
from streamlit_lottie import st_lottie
import json
from aiinterview import chatConversation,get_feedback

def query(OPENAI_API_KEY):
    # percentage=0
    if "jobdescription" not in st.session_state:
        st.session_state.jobdescription=None
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "count" not in st.session_state:
        st.session_state.count=0
# Initialize chat history
    jd = st.text_area("Please enter the job description here (If you don't have one, enter keywords, such as PostgreSQL or Python instead): ")
    st.session_state.jobdescription=jd
    print(len(st.session_state.messages))
    
    if len(st.session_state.messages)>=17:
        if st.button("Generate Feedback"):
            # print(st.session_state.messages,88888888888888888888)
            feedback_response=get_feedback(st.session_state.messages[2:],"please provide feedback of my interview process",OPENAI_API_KEY)
            if feedback_response:   
                st.session_state.messages=[]
                st.session_state.count=0
                st.session_state.jobdescription=None
                placeholder=st.empty()
                full_response = ""
                for chunk in feedback_response:
                    full_response+=chunk.content
                    if bool(chunk):
                        time.sleep(0.02)
                        placeholder.markdown(full_response + "")
                placeholder.markdown(full_response)
                st.download_button(label="Download Interview Feedback", data=full_response, file_name="interview_feedback.txt")
                st.stop()
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    jobdescription_and_skills={"job_description_is":jd}
    if st.session_state.jobdescription:
        if st.session_state.count==0:
            st.write("Type hi below to start...")
            st.session_state.count=1
        
        if answer := st.chat_input("write your answer here..."):
            st.session_state.messages.append({"role": "user", "content": answer})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(answer)
            with st.spinner("thinking..."):
                response=chatConversation(answer,jobdescription_and_skills,OPENAI_API_KEY)
            if response:
            # Display assistant response in chat message container
                with st.chat_message(name="assistant"):
                    message_placeholder = st.empty()
                    full_response = ""
                    for chunk in response['text'].split():
                        full_response += chunk + " "
                        time.sleep(0.05)
                        message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            else:
                st.warning("Invalid API key")
                st.session_state.messages=[]

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
st_lottie(load_lottiefile("welcome.json"), speed=1, reverse=False, loop=True, quality="high", height=300)
with st.sidebar:
    OPENAI_API_KEY=st.text_input(placeholder="OPENAI API KEY",label="OPENAI API KEY",type="password",key="OPENAI_API_KEY",label_visibility="collapsed")

if OPENAI_API_KEY:
    query(OPENAI_API_KEY)
    
    
 