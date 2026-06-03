from typing import TypedDict, List
from langchain_core.messages import BaseMessage
from langgraph.graph.message import Annotated, add_messages


class ResearchAgentState(TypedDict):
    
    query: str
    task: str
    
    messages: Annotated[List[BaseMessage], add_messages]
    