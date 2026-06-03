from tools.search_tool import search_tool
from langgraph.prebuilt import ToolNode

tools = [search_tool]

tools_node = ToolNode(tools)