from state.agent_state import AgentState
from agents.supervisor_agent import SupervisorAgent

async def supervisor_node(state: AgentState) -> dict:
    decider_output = state.get('decider_output', []).get('output', [])
    agent = SupervisorAgent()
    
    if decider_output:
        result = await agent.delegate_parallel(decider_output)
        return {"supervisor_output": result}
    
    return {"supervisor_output": "No tasks to delegate."}