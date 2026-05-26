import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()
huggingface_api_key = os.getenv('HUGGINGFACE_API_KEY')

model = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    huggingfacehub_api_token=huggingface_api_key
)

llm = ChatHuggingFace(llm=model)