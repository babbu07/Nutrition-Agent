from agents.base_agent import BaseAgent
from schemas.agent_output_schema import AgentOutput
from graph.research_graph import research_graph

class ResearchAgent(BaseAgent):

    name = "research_agent"
    description = "Handles research and information gathering tasks"

    async def execute(self, user_query: str, task: str, agent_input: dict, state: dict) -> AgentOutput:
        # Execute the research graph with the provided inputs
        state['query'] = user_query
        state['task'] = task
        result = await research_graph.ainvoke(state)
        
        return AgentOutput(
            agent=self.name,
            success=True,
            content=result['messages'][-1].content,
            metadata={"agent": self.name}
        )