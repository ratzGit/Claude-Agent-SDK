import asyncio
from claude_agent_sdk import query


async def main():
    async for message in query(
        prompt="Say hello world in a quirky way.",       
    ):
        if hasattr(message, "result"):
            print(message.result)

asyncio.run(main())