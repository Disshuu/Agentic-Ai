from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from rag.loader import load_pdf, load_txt
from rag.store import add_document
from core.pipeline import pipeline

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

# 🔹 Upload Endpoint
@app.post("/upload")
async def upload(file: UploadFile = File(...)):

    if file.filename.endswith(".pdf"):
        text = load_pdf(file.file)

    elif file.filename.endswith(".txt"):
        text = load_txt(file.file)

    else:
        return {"error": "Unsupported file"}

    add_document(text)
    return {"message": "Document uploaded successfully"}


# 🔥 STREAMING RUN-TASK
@app.post("/run-task")
async def run_task(request: TaskRequest):

    async def stream():
        async for step in pipeline(request.task):
            yield step

    return StreamingResponse(stream(), media_type="text/plain")


# 🔹 Home
@app.get("/")
def home():
    return {"message": "Agentic AI system running"}