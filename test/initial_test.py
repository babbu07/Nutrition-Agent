from graph.main_graph import graph
import asyncio


def run():
    state = {
        "user_input": {
            "query": "What is the capital of France?"
        }
    }


    result = asyncio.run(graph.ainvoke(state))
    return result

if __name__ == "__main__":
    
    print(run())
