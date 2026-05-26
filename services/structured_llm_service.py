from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import os
from dotenv import load_dotenv

load_dotenv()
huggingface_api_key = os.getenv('HUGGINGFACE_API_KEY')

llm_huggingface = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2.5-7B-Instruct',
    huggingfacehub_api_token=huggingface_api_key
)

structured_llm = ChatHuggingFace(llm=llm_huggingface)
