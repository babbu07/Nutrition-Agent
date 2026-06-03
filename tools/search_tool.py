from tavily import TavilyClient
from dotenv import load_dotenv
from langchain.tools import tool
from schemas.tool_output import ToolOutput
import os

load_dotenv()
tavily_api_key = os.getenv('TAVILY_API_KEY')

       
@tool
def search_tool(query: str, max_results: int = 3):
    """Searches the web for the given query and returns the top results."""
    client = TavilyClient(api_key=tavily_api_key)
    result = client.search(query=query, max_results=max_results)
        
    formatted = []
    for r in result['results']:
        formatted.append(f"{r['title']}: {r['content']}")
    
    return "\n".join(formatted)
     