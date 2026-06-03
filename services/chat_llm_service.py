from langchain_ollama import ChatOllama

# Initialize ChatOllama pointing to your local qwen instance
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0,               # 0 ensures strict, reliable tool choices
    base_url="http://localhost:11434"
)