from agents.base_agent import BaseAgent
from schemas.agent_output_schema import AgentOutput


class RAGAgent(BaseAgent):

    name = "rag_agent"
    description = "Handles knowledge retrieval"

    async def execute(self, user_query: str, task: str, agent_input: dict) -> AgentOutput:
        return AgentOutput(
            agent=self.name,
            success=True,
            content=f"RAGAgent received query: {user_query} with task: {task} and input: {agent_input}",
            metadata={"agent": self.name}
        )