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
from instruction import instructionForBot1, feedback_template, feedback_analytics
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "{instructionForBot}{jobdescription_and_skills}"),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question},")], input_variables=["instruction_for_bot", "jobdescription_and_skills"])
memory = ConversationBufferWindowMemory(
    memory_key="chat_history", return_messages=True, input_key="question", k=7)


def chatConversation(answer, jobdescriptionSkills, OPENAI_API_KEY):
    try:
        llm = ChatOpenAI(temperature=0.0, model="gpt-3.5-turbo",
                         api_key=OPENAI_API_KEY)
        conversation_chain = LLMChain(
            llm=llm, prompt=prompt, memory=memory)
        response = conversation_chain(
            {"question": answer, "instructionForBot": instructionForBot1, "jobdescription_and_skills": jobdescriptionSkills})
        return response
    except openai.AuthenticationError as e:
        return None


def get_feedback(history, input_question, OPENAI_API_KEY):
    messages = [
        SystemMessage(
            content=f"""{feedback_template}{history}"""
        ),
        HumanMessage(
            content=input_question
        )]
    chat = ChatOpenAI(streaming=True, temperature=0.0, api_key=OPENAI_API_KEY)
    response = chat.invoke(messages)
    return response


class Feedback(BaseModel):
    confidence_level: int = Field(
        description="this field contains the value of confidence")
    technical_skill: int = Field(
        description="this field contains the value of technical knowledge")
    accurate_answer: int = Field(
        description="this field contains the value of accurate answers")
    total_score: int = Field(
        description="this field contains the total score in interview session")


def get_feedback_analytics(feedback_instruction, interview_history, OPENAI_API_KEY):

    parser = JsonOutputParser(pydantic_object=Feedback)
    prompt_for_feedback_analytics = PromptTemplate(input_variables=["feedback_instruction", "interview_history"],
                                                   template="{feedback_instruction} {interview_history}",
                                                   partial_variables={"format_instructions": parser.get_format_instructions()})

    llm_model = ChatOpenAI(temperature=0.2, api_key=OPENAI_API_KEY)

    enhance_content_chain = prompt_for_feedback_analytics | llm_model | parser

    response = enhance_content_chain.invoke(
        {"feedback_instruction": feedback_instruction, "interview_history": interview_history})
    return response
