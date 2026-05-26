from pydantic import BaseModel
from typing import List, Literal, Dict, Any

class AgentInput(BaseModel):

    agent_name: Literal["memory_agent", "research_agent", "rag_agent"]
    query: str
    task: str
    agent_input: Dict[str, str] = {}

class DeciderOutput(BaseModel):

    output: List[AgentInput]