"""create_vectorstore.py module."""
import os
from dotenv import load_dotenv

from src.loader import load_documents
from src.splitter import split_documents
from src.embedder import embedder
from src.vectorstore import create_vectorstore


## Configura LangSmith
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
LANGCHAIN_API_KEY = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "lgpd-vectorstore-creation"

## Carregar arquivos LGPD
documents = load_documents()
## Criar chunks
doc_chunks = split_documents(documents)
## Definir embedder
embedding = embedder()
## Armazenar embrddings no vectorstore
vectorstore = create_vectorstore(doc_chunks, embedding)

