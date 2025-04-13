import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain



load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


# STEP 4: Define a simple prompt template for customer support
prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a helpful and knowledgeable assistant.

Question: {question}

Answer:"""
)

# STEP 5: Connect the model and prompt in a LangChain LLMChain
chain = prompt | llm

def get_bot_response(question: str) -> str:
    response = chain.invoke({"question": question})
    return response.content if hasattr(response, "content") else str(response)
