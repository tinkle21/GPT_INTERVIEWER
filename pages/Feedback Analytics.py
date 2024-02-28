from instruction import feedback_analytics
import streamlit as st
import time
from PIL import Image
from aiinterview import get_feedback_analytics, get_feedback

if "display_analytics" not in st.session_state:
    st.session_state.display_analytics = False

if "feedback_response" not in st.session_state:
    st.session_state.feedback_response = None

if st.session_state.display_analytics:
    if st.session_state.feedback_response is None:
        with st.spinner("processing"):
            feedback_response = get_feedback_analytics(
                feedback_analytics, st.session_state.messages, st.session_state.open_api_key)
            st.session_state.feedback_response = feedback_response
if st.session_state.feedback_response:
    col1, col2 = st.columns(2)
    with col1:
        st.header("Confidence Score")
        progress_text = "Communication Skills"
        my_bar = st.progress(0, text=f"{0}%")

        for i in range(100):
            time.sleep(0.01)
            if i == st.session_state.feedback_response["confidence_level"]:
                break
            my_bar.progress(i + 1, text=f"{i}%")
        time.sleep(1)

    with col2:
        st.header("Technical Score")
        progress_text = "TECHNICAL SKILLS"
        my_bar2 = st.progress(0, text=f"{0}%")

        for i in range(100):
            time.sleep(0.01)
            if i == st.session_state.feedback_response["technical_skill"]:
                break
            my_bar2.progress(i + 1, text=f"{i}%")
        time.sleep(1)

    col3, col4 = st.columns(2)
    with col3:
        st.header("Correctness Score")
        progress_text = "Knowledge"
        my_bar2 = st.progress(0, text=f"{0}%")

        for i in range(100):
            time.sleep(0.01)
            if i == st.session_state.feedback_response["accurate_answer"]:
                break
            my_bar2.progress(i + 1, text=f"{i}%")
        time.sleep(1)

    with col4:
        st.header("OverAll Score")
        progress_text = "Interview Score"
        my_bar2 = st.progress(0, text=f"{0}%")
        for i in range(100):
            time.sleep(0.01)
            if i == st.session_state.feedback_response["total_score"]:
                break
            my_bar2.progress(i + 1, text=f"{i}%")
        time.sleep(1)

    if st.button("Generate more Feedback"):
        feedback_response = get_feedback(
            st.session_state.messages, "please provide feedback of my interview process", st.session_state.open_api_key)
        if feedback_response:
            st.download_button(label="Download Interview Feedback",
                               data=feedback_response.content, file_name="interview_feedback.txt")
            st.session_state.jobdescription = None
            st.session_state.messages = []
            st.session_state.open_api_key = None
            st.session_state.count = 0
            st.session_state.feedback_response = None
            st.session_state.display_analytics = False
            st.stop()
if not st.session_state.display_analytics:
    im = Image.open("icon.png")
    home_title = "AI Interviewer"
    home_introduction = "Welcome to AI Interviewer, empowering your interview preparation with generative AI."
    st.markdown(
        "<style>#MainMenu{visibility:hidden;}</style>",
        unsafe_allow_html=True
    )
    st.image(im, width=100)
    st.markdown(
        f"""# {home_title}""", unsafe_allow_html=True)
    st.markdown("""\n""")
    st.markdown("##### Welcome to AI Interviewer! 👏 AI Interviewer is your personal interviewer powered by generative AI that conducts interviews."
                "You can enter job descriptions, and AI Interviewer will ask you customized questions.")
    st.markdown("""\n""")
    st.markdown("## Get started!")
    st.markdown(
        "#### Select Technical Interview Screen From Side Bar to start your interview!")
    st.markdown(
        "#### After the Interview You can see your Analytics here!Thank you")
