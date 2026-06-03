from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition
from nodes.research_nodes.brain_node import brain_node
from nodes.research_nodes.tools_node import tools_node
from state.research_state import ResearchAgentState

builder = StateGraph(ResearchAgentState)

builder.add_node('brain', brain_node)
builder.add_node('tools', tools_node)

builder.add_edge(START, 'brain')
builder.add_conditional_edges('brain', tools_condition)
builder.add_edge('tools', 'brain')

research_graph = builder.compile()
