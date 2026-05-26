from agents.base_agent import BaseAgent
from schemas.agent_output_schema import AgentOutput

class ResearchAgent(BaseAgent):

    name = "research_agent"
    description = "Handles research and information gathering tasks"

    async def execute(self, user_query: str, task: str, agent_input: dict) -> AgentOutput:
        return AgentOutput(
            agent=self.name,
            success=True,
            content=f"ResearchAgent received query: {user_query} with task: {task} and input: {agent_input}",
            metadata={"agent": self.name}
        )