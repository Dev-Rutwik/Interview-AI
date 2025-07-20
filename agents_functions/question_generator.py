from config.mistral_config import llm
from langchain_core.prompts import ChatPromptTemplate
SYSTEM_MESSAGE = "You are an interviewer."

initial_question_prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_MESSAGE),
    ("human", 
     "Based on this resume cluster content, generate one concise interview question:\n\n{cluster_content}\n\nOnly return the question in one or two sentences. No extra text.")
])

followup_check_prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_MESSAGE),
    ("human",
     "Look at this user response and decide if a follow-up question is needed.\n\nAnswer: {user_response}\n\n"
     "If the answer is big and detailed, return JSON:\n{{\"follow_up_needed\": true}}\n\n"
     "If the answer is short, yes, no, 'I don't know', or incorrect, return:\n{{\"follow_up_needed\": false}}\n\n"
     "Only return the JSON. No extra text.")
])


followup_question_prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_MESSAGE),
    ("human",
     "Based on this question and the user's answer, create a follow-up question.\n\n"
     "Question: {question}\n"
     "Answer: {user_response}\n\n"
     "Only return the follow-up question. No extra text.")
])


def generate_initial_question(cluster_content):
    prompt = initial_question_prompt.format_messages(cluster_content=cluster_content)
    return llm.invoke(prompt).content

def is_followup_req(user_response):
    prompt = followup_check_prompt.format_messages(user_response=user_response)
    return llm.invoke(prompt).content

def generate_followup_question(question, user_response):
    prompt = followup_question_prompt.format_messages(question=question, user_response=user_response)
    return llm.invoke(prompt).content


