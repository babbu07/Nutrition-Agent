from abc import ABC, abstractmethod
from schemas.agent_output_schema import AgentOutput

class BaseAgent(ABC):
    name: str
    description: str
    @abstractmethod
    async def execute(self, user_query: str, task: str, agent_input: dict) -> AgentOutput:
        pass