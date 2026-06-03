from langchain_core.messages import SystemMessage, HumanMessage
from state.research_state import ResearchAgentState
from services.chat_llm_service import llm
from tools.search_tool import search_tool
from prompts.ResearchAgent.brain_node_prompt import BRAIN_PROMPT

def brain_node(state: ResearchAgentState) -> dict:
    tools = [search_tool]
    llm_tools = llm.bind_tools(tools)
    
    system_instruction = SystemMessage(
        content=f"{BRAIN_PROMPT}\n\nQuery Context: {state.get('query', '')}\nTask Context: {state.get('task', '')}"
    )
    
    history = state.get("messages", [])
    if not history:
        history = [HumanMessage(content=f"Please execute research task for: {state.get('query', '')}")]
    
    full_payload = [system_instruction] + history
    response = llm_tools.invoke(full_payload)
    
    return {
        'messages': [response]
    }