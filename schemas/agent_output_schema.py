from pydantic import BaseModel
from typing import Dict, Any, Literal


class AgentOutput(BaseModel):

    success: bool
    agent: Literal["memory_agent", "research_agent", "rag_agent"]
    content: str
    metadata: Dict[str, Any] = {}