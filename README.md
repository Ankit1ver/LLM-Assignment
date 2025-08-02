# RAG Pipeline App

This project implements a Retrieval-Augmented Generation (RAG) pipeline using FastAPI, FAISS, LangChain, and OpenAI.

## 🚀 Features
- Upload up to 20 PDF files
- Chunk and embed using OpenAI + FAISS
- Ask context-aware questions using GPT-3.5
- REST API via FastAPI
- Dockerized for local/cloud deployment

## 🛠️ Setup Instructions

### 1. Clone & Configure
```bash
git clone https://github.com/yourusername/rag-pipeline
cd rag-pipeline
echo "OPENAI_API_KEY=your-key-here" > .env
```

### 2. Run Locally (No Docker)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Run with Docker
```bash
docker-compose up --build
```

## 📡 API Endpoints

### POST /upload
Upload one or more PDFs:
```bash
curl -X POST http://localhost:8000/upload \
  -F "files=@yourfile1.pdf" \
  -F "files=@yourfile2.pdf"
```

### POST /query
Ask a question:
```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is this document about?"}'
```

## ✅ TODO
- Add metadata storage
- Add Postman collection
- Add unit tests

---
MIT License © 2025
