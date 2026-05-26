from schemas.decider_output import DeciderOutput
from services.structured_llm_service import structured_llm
from prompts.decider_prompt import DECIDER_PROMPT
from state.agent_state import AgentState


def decider_node(state: AgentState) -> dict:
    decider_llm = structured_llm.with_structured_output(DeciderOutput, method='json_mode')
    user_input = state.get('user_input', {})
    
    prompt = DECIDER_PROMPT + f"\n\n You have been given the following user input:\n\nUser Input: {user_input}"
    
    response = decider_llm.invoke(prompt)
    
    return {'decider_output': response}