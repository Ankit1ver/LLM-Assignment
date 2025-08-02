from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
import os
import shutil
import uuid
from dotenv import load_dotenv

from services.document_handler import process_documents
from services.rag_pipeline import ask_question

load_dotenv()

app = FastAPI()
UPLOAD_DIR = "uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class QueryRequest(BaseModel):
    query: str

@app.post("/upload")
async def upload_docs(files: List[UploadFile] = File(...)):
    file_paths = []
    for file in files:
        file_id = str(uuid.uuid4())
        file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        file_paths.append(file_path)

    process_documents(file_paths)
    return JSONResponse(content={"message": "Files uploaded and processed", "files": file_paths})

@app.post("/query")
async def query_docs(query_req: QueryRequest):
    answer = ask_question(query_req.query)
    return {"query": query_req.query, "answer": answer}
