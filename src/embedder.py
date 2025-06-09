"""embedder.py module."""
import os
from langchain_huggingface import HuggingFaceEmbeddings
from src.config import EMBEDDING_MODEL

# Desabilita warning
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

def embedder():
    """
    Inicializa e retorna um modelo de embedding.
    """
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
