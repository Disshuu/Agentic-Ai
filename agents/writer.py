import asyncio

async def writer(insights, task):
    await asyncio.sleep(0.5)

    output = f"\n📄 FINAL REPORT for: {task}\n\n"

    # SUMMARY
   # SUMMARY
    output += "🔹 Summary:\n"

    if insights:
        text = insights[0].lower()
 
        if "student" in text or "skills" in text:  
            output += "The document appears to be a professional profile or resume highlighting skills, experience, and career objectives.\n\n"
        elif "internship" in text:
            output += "The document describes an internship program, including its structure and requirements.\n\n"
        else:
            output += insights[0] + ".\n\n"
    else:
        output += "No meaningful data found.\n\n"

    output += "🔹 Key Insights:\n"
    for i, ins in enumerate(insights):
        output += f"{i+1}. {ins}\n"

    output += "\n🔹 Conclusion:\n"
    if insights:
        output += "The document contains relevant extracted insights based on semantic retrieval and analysis.\n"
    else:
        output += "No sufficient insights could be extracted.\n"

    return output