from agents.base_agent import BaseAgent
from schemas.agent_output_schema import AgentOutput

class MemoryAgent(BaseAgent):

    name = "memory_agent"
    description = "Handles User Memory and Retrieve Memory"

    async def execute(self, user_query: str, task: str, agent_input: dict, state: dict) -> AgentOutput:
        return AgentOutput(
            agent=self.name,
            success=True,
            content=f"MemoryAgent received query: {user_query} with task: {task} and input: {agent_input}",
            metadata={"agent": self.name}
        )