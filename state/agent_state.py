from typing import TypedDict, List, Dict, Any, Annotated
from langchain_core.messages import BaseMessage
from schemas.decider_output import DeciderOutput
import operator


class AgentState(TypedDict):
    
    thread_id: str
    user_id: str
    
    messages: Annotated[List[BaseMessage], operator.add]
    user_input: Dict[str, str]

    decider_output: DeciderOutput
    supervisor_output: List[Dict[str, Any]]
    response: str
    