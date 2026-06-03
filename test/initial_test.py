from graph.main_graph import graph
import asyncio


def run():
    state = {
        "user_input": {
            "query": "which is the most trending news today?"
        }
    }


    result = asyncio.run(graph.ainvoke(
        state,
        config={
            "configurable": {"thread_id": "user_session_42"}
        }
    ))
    return result

if __name__ == "__main__":
    
    print(run())
