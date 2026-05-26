from nodes.decider_node import decider_node
from nodes.supervisor_node import supervisor_node
from nodes.response_node import response_node
from state.agent_state import AgentState

from langgraph.graph import StateGraph, START, END

builder = StateGraph(AgentState)

builder.add_node("decider_node", decider_node)
builder.add_node("supervisor_node", supervisor_node)
builder.add_node("response_node", response_node)

builder.add_edge(START, "decider_node")
builder.add_edge("decider_node", "supervisor_node")
builder.add_edge("supervisor_node", "response_node")
builder.add_edge("response_node", END)

graph = builder.compile()