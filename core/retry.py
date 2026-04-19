import asyncio

async def safe_execute(agent, data, retries=3):
    for attempt in range(retries):
        try:
            return await agent(data)
        except Exception:
            await asyncio.sleep(1)
    return []