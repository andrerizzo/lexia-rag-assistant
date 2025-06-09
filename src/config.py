"""config.py module."""
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

## Documents
DATA_DIR = "data"

## Splitter
# -------------------
#      INICIAL
# -------------------
#CHUNK_SIZE = 1000
#CHUNK_OVERLAP = 50

## Embedder
#EMBEDDING_MODEL = "text-embedding-3-large"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"

## Vector db
#DB_NAME = "lgpd_database"
DB_COLLECTION = "lgpd_database"
DB_DIRECTORY = os.path.join("data", DB_COLLECTION)

## Frontier model
LLM_MODEL = "gpt-4o"
MODEL_PROVIDER = "openai"
TEMPERATURE = 0.7


