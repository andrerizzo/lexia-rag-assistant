"""splitter.py module."""
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.logger import get_logger

def split_documents(docs):
    """
    Divide documentos em trechos (chunks) menores para uso em pipelines 
    de NLP ou RAG.

    Utiliza o RecursiveCharacterTextSplitter para segmentar os documentos 
    mantendo coerência textual, respeitando o tamanho definido e a 
    sobreposição entre os trechos.

    Parameters:
        docs (list): Lista de documentos (Document) a serem divididos.
        chunk_size (int, optional): Tamanho máximo de cada chunk. 
        Padrão é 1000 caracteres.
        chunk_overlap (int, optional): Número de caracteres de 
        sobreposição entre chunks. Padrão é 50.
    """
    logger = get_logger(__name__)
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, 
                                              chunk_overlap=50,
                                              add_start_index=True,
                                              separators=["\n\n\n", "\n\n", "\n", ".", ";", ","]
    )
    splitted_docs = splitter.split_documents(docs)
    
    logger.info("Total de chunks gerados: %s", len(splitted_docs))
    return splitted_docs

