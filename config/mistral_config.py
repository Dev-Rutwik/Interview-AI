import os
from dotenv import load_dotenv
from langchain_mistralai.chat_models import ChatMistralAI

load_dotenv()

llm = ChatMistralAI(
    model="mistral-small",
    api_key=os.getenv("MISTRAL_API_KEY")
)
