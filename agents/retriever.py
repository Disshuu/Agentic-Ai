from rag.store import search
import asyncio

async def retriever(task):
    await asyncio.sleep(1)
    data = search(task)
    return data