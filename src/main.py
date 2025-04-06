import os
from langchain.llms import HuggingFaceHub
from huggingface_hub import login
from langchain import PromptTemplate, LLMChain


os.environ["HUGGINGFACEHUB_API_TOKEN"] = "key"
login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1",
    model_kwargs={"temperature": 0.5, "max_new_tokens": 200}
)

# STEP 4: Define a simple prompt template for customer support
prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a helpful and knowledgeable assistant.

Question: {question}

Answer:"""
)

# STEP 5: Connect the model and prompt in a LangChain LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

def get_bot_response(question: str) -> str:
    return chain.run(question=question)
