from agents.research_agent import ResearchAgent
from langchain.messages import HumanMessage
import asyncio


def run():

    result = asyncio.run(ResearchAgent().execute(
        user_query="give me 3 latest news about AI.",
        task="research",
        agent_input={},
        state={
            'messages': [HumanMessage(content="give me 3 latest news about AI.")]
        }
    ))
    return result

if __name__ == "__main__":
    
    print(run())
