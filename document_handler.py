import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

DB_DIR = "vectorstore/db"
os.makedirs(DB_DIR, exist_ok=True)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
embedding_model = OpenAIEmbeddings()

def process_documents(file_paths):
    docs = []
    for file_path in file_paths:
        loader = PyPDFLoader(file_path)
        pages = loader.load()
        split_docs = text_splitter.split_documents(pages)
        docs.extend(split_docs)

    vectordb = FAISS.from_documents(docs, embedding_model)
    vectordb.save_local(DB_DIR)
