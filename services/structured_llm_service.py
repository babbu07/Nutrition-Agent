from langchain_ollama import ChatOllama


structured_llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0,
    format="json",
    base_url="http://localhost:11434"
)
