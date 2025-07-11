from config.mistral_config import llm

def generate_initial_question(cluster_content):
    prompt = f"""
    Based on this resume cluster content, generate one concise interview question:
    {cluster_content}
    
    Generate only the question in one or two sentence, no additional text.
    """
    return llm.invoke(prompt).content

def generate_followup_question(question, user_response):
    prompt = f"""
    Based on this interview exchange, generate one concise follow-up question:
    Question: {question}
    Answer: {user_response}
    
    Generate only the question one or two sentence, no additional text.
    """
    return llm.invoke(prompt).content
