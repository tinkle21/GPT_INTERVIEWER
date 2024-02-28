import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

im = Image.open("icon.png")
st.set_page_config(page_title = "AI Interviewer", layout = "centered",page_icon=im)
home_title = "AI Interviewer"
home_introduction = "Welcome to AI Interviewer, empowering your interview preparation with generative AI."
with st.sidebar:
    pass
st.markdown(
    "<style>#MainMenu{visibility:hidden;}</style>",
    unsafe_allow_html=True
)
st.image(im, width=100)
st.markdown(f"""# {home_title}""",unsafe_allow_html=True)
st.markdown("""\n""")
st.markdown("Welcome to AI Interviewer! 👏 AI Interviewer is your personal interviewer powered by generative AI that conducts interviews."
            "You can enter job descriptions, and AI Interviewer will ask you customized questions.")
st.markdown("""\n""")
st.markdown("#### Get started!")
st.markdown("Select one of the following screens to start your interview!")
selected = option_menu(
        menu_title= None,
        options=["Technical Interview","Help"],
        icons = ["cast","help"],
        default_index=0,
        orientation="horizontal",
    )
if selected == 'Technical Interview':
        st.info("""
            📚In this session, the AI Interviewer will assess your technical skills as they relate to the job description.
            Note: The maximum length of your answer is 4097 tokens!
            - Each Interview will take 10 to 15 mins.
            - To start a new session, just refresh the page.
            - Start introduce yourself and enjoy！ """)
        if st.button("Start Interview!"):
            st.switch_page("pages/Technical Interview.py")
if selected == 'Help':
    website="https://platform.openai.com/api-keys"
    st.info(f"""📚Firstly, You have to put OPEN AI API key in the side bar to start the interview process.
            To get your keys you have to visit {website} .
            """)
    