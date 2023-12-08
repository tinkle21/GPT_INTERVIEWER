import streamlit as st
import time
from streamlit_tags import st_tags
from aiinterview import chatConversation

def query(total_Skills,openai_api_key):
# Initialize chat history
    jd = st.text_area("Please enter the job description here (If you don't have one, enter keywords, such as PostgreSQL or Python instead): ")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    if "count" not in st.session_state:
        st.session_state.count=0

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    jobdescription_and_skills={"job_description_is":jd,"skills of user":total_Skills[:]}
    print(jd,888888888888888888888)
    if jd:
        if st.session_state.count==0:
            st.write("Type hi below to start...")
            st.session_state.count=1
        if answer := st.chat_input("write your response here..."):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": answer})
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(answer)
            with st.spinner("thinking..."):
                response=chatConversation(answer,jobdescription_and_skills,openai_api_key)
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


st.title(":blue[AI INTERVIEWER]")
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key",type="password")
    st.header('TECHNICAL SKILLS',divider='rainbow')
    total_Skills = st_tags(label='ENTER YOUR SKILLS',
            text='Please add more Skills',
            value=['Machine Learning'],
            suggestions=[],
            maxtags = 5,
            key='1')
query(total_Skills,openai_api_key)
    
    
 