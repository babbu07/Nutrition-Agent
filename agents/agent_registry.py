from agents.research_agent import ResearchAgent
from agents.memory_agent import MemoryAgent
from agents.rag_agent import RAGAgent


AGENTS = {
    "research_agent": ResearchAgent(),

    "memory_agent": MemoryAgent(),
    
    "rag_agent": RAGAgent()
}