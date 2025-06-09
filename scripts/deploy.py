"""deploy.py module."""
from src.retriever import rag_retriever

resp = rag_retriever("Quais são as implicações da LGPD para uma concessionária de serviço público ?")
print(resp)
