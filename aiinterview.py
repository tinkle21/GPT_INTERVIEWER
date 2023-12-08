from langchain.memory import ConversationSummaryMemory
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain.chat_models import ChatOpenAI


instruction_for_bot = f"Your name is GPTInterviewer.I want you to act as an interviewer strictly following the guideline in the context.Candidate has no idea what the guideline is.Do not give explanations for right answers.Ask question like a real person, only one question at a time.you should mostly ask questions that have more accurate answer.Do not ask the same question again.Do ask follow-up questions if necessary.Make sure the questions tests the technical knowledge.I want you to only reply as an interviewer.Do not write all the conversation at once.If there is an error, point it out.Interview will end if any condition satisfy (10 minutes or 15 question).Then share the feedback to user based on the interview session if user ask for it, interviewer response will not be more than 50 words"
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "{instruction_for_bot}you will get the job descriptions or Skills,check that if job description provided is valid or not if not then use the skills context for asking questions otherwise prefer the job description for asking question and then tell him ,Hello, Welcome to the interview. I am your interviewer today. I will ask you technical questions regarding the job description or skills you submitted.Please start by introducting a little bit about yourself, then you start your interview process by asking questions , this is the job desciption and skills provided to you {jobdescription_and_skills}"),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question},")], input_variables=["instruction_for_bot","jobdescription_and_skills"])




def chatConversation(answer,jobdescriptionSkills,openai_api_key):
    llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo",api_key=openai_api_key)
    memory = ConversationSummaryMemory(llm=llm,
    memory_key="chat_history", return_messages=True, input_key="question")
    conversation = LLMChain(llm=llm, prompt=prompt, verbose=True, memory=memory)
    with get_openai_callback() as cb:
        response = conversation(
            {"question": answer, "instruction_for_bot": instruction_for_bot,"jobdescription_and_skills":jobdescriptionSkills})
        return response
    
    
    
    
    