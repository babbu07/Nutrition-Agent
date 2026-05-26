from state.agent_state import AgentState
from services.chat_llm_service import llm
from prompts.response_prompt import RESPONSE_PROMPT

def response_node(state: AgentState) -> dict:
    supervisor_output = state.get('supervisor_output', "No output from supervisor.")
    user_input = state.get('user_input', "No user input.")
    
    prompt = RESPONSE_PROMPT + f"\n\nUser Input:\n{user_input}\n\nSupervisor Output:\n{supervisor_output}"
    response = llm.invoke(prompt)
    
    return {"response": response}