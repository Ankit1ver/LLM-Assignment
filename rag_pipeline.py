from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

DB_DIR = "vectorstore/db"

retriever = FAISS.load_local(DB_DIR, OpenAIEmbeddings()).as_retriever()
llm = ChatOpenAI(temperature=0.2, model_name="gpt-3.5-turbo")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def ask_question(query):
    return qa.run(query)
