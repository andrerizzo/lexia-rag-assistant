"""api.py module."""
from fastapi import FastAPI
from pydantic import BaseModel
from src.retriever import rag_retriever

app = FastAPI(title="LGPD RAG Test API", 
              description="API simples para testar o sistema RAG", 
              version="0.1.0"
              )

#@app.get("/generate")
#def generate(question: str):
#    response = rag_retriever(question)
#    return response

class Question(BaseModel):
    question: str

@app.post("/rag")
def rag(data: Question):
    response = rag_retriever(data.question)
    return {"response": response}
