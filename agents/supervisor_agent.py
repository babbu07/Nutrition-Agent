import asyncio
from agents.agent_registry import AGENTS


class SupervisorAgent:

    async def delegate(self, agent_name, query, task, agent_input, state):

        agent = AGENTS.get(agent_name)

        if not agent:
            return {
                "success": False,
                "agent": agent_name,
                "content": (
                    f"Unknown agent:"
                    f"{agent_name}"
                ),
                "metadata": {"error": True}
            }

        try:
            result = await agent.execute(user_query=query, task=task, agent_input=agent_input, state=state)
            return result

        except Exception as e:
            return {
                "success": False,
                "agent": agent_name,
                "content": str(e),
                "metadata": {"error": True}
            }
        
    async def delegate_parallel(self, tasks, state):

        coroutines = []
        for item in tasks:

            coroutine = self.delegate(
                agent_name=item.agent_name,
                query=item.query,
                task=item.task,
                agent_input=item.agent_input,
                state=state
            )

            coroutines.append(coroutine)

        return await asyncio.gather(*coroutines)