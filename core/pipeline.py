import asyncio

from agents.retriever import retriever
from agents.analyzer import analyzer
from agents.writer import writer
from core.queue import push_task, pop_task
from core.retry import safe_execute
from core.planner import plan_task


async def pipeline(task):

    yield "\n==============================\n"
    yield "🧠 TASK EXECUTION STARTED\n"
    yield "==============================\n\n"

    await asyncio.sleep(0.3)

    yield f"📌 Task: {task}\n\n"

    # 🔹 PLAN
    steps = plan_task(task)
    yield "🧩 Planning:\n"
    for s in steps:
        yield f"- {s['step']}\n"
    yield "\n"

    await asyncio.sleep(0.3)

    # 🔹 PUSH FIRST TASK
    push_task({"step": "retrieve", "data": task})

    context = None
    insights = None

    while True:
        current = pop_task()
        if not current:
            break

        step = current["step"]
        data = current["data"]

        # 🔍 RETRIEVER
        if step == "retrieve":
            yield "🔍 Retriever running...\n"
            await asyncio.sleep(0.5)

            context = await safe_execute(retriever, data)

            for c in context:
                yield f"- {c[:100]}...\n"

            yield "\n"

            push_task({"step": "analyze", "data": context})

        # 📊 ANALYZER
        elif step == "analyze":
            yield "📊 Analyzer running...\n"
            await asyncio.sleep(0.5)

            insights = await safe_execute(analyzer, data)

            for i in insights:
                yield f"• {i}\n"

            yield "\n"

            push_task({"step": "write", "data": insights})

        # ✍️ WRITER
        elif step == "write":
            yield "✍️ Writer generating output...\n"
            await asyncio.sleep(0.5)

            final = await writer(data, task)

            yield final
            break

    yield "\n✅ TASK COMPLETED\n"