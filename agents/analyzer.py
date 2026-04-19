import asyncio
import re

async def analyzer(data):
    await asyncio.sleep(0.5)

    if not data:
        return ["No relevant data found"]

    insights = []
    fallback = None

    for d in data:
        d = " ".join(d.split())

        sentences = re.split(r"[.?!]", d)

        for s in sentences:
            s = s.strip()
            # ❌ remove merged heading text (IMPORTANT FIX)
            if len(s.split()) < 6:
                continue
            if sum(1 for c in s if c.isupper()) > len(s) * 0.5:
                continue
            if s.isupper():
                continue
            # remove noise
            if (
                len(s) < 30 or
                "chapter" in s.lower() or
                "figure" in s.lower() or
                "table" in s.lower() or
                "sincerely" in s.lower() or
                "thank" in s.lower()
            ):
                continue

            # shorten long sentences (🔥 important)
            if len(s) > 120:
                s = s[:120] + "..."

            if not fallback:
                fallback = s

            insights.append(s)

    insights = list(dict.fromkeys(insights))

    if not insights and fallback:
        insights.append(fallback)

    if not insights:
        return ["No meaningful insights found"]

    return insights[:4]