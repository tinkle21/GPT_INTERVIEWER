from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
import openai
from langchain.schema import HumanMessage, SystemMessage
from instruction import instructionForBot1,feedback_template
from langchain_openai  import ChatOpenAI


prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "{instructionForBot}{jobdescription_and_skills}"),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question},")], input_variables=["instruction_for_bot","jobdescription_and_skills"])
memory = ConversationBufferWindowMemory(memory_key="chat_history", return_messages=True, input_key="question",k=7)



def chatConversation(answer,jobdescriptionSkills,OPENAI_API_KEY):
    try:
        llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo",api_key=OPENAI_API_KEY)
        conversation_chain = LLMChain(llm=llm, prompt=prompt, verbose=True, memory=memory)
        response = conversation_chain(
                {"question": answer, "instructionForBot": instructionForBot1,"jobdescription_and_skills":jobdescriptionSkills})
        return response
    except openai.AuthenticationError as e:
        return None
    


def get_feedback(history,input_question,OPENAI_API_KEY):
    messages = [
    SystemMessage(
        content=f"""{feedback_template}{history}"""
    ),
    HumanMessage(
        content=input_question
    )]
    chat = ChatOpenAI(streaming=True,temperature=0.0,api_key=OPENAI_API_KEY)
    response=chat.stream(messages)
    return response