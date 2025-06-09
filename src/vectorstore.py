"""vectorstore.py module."""
import os
import faiss
from langchain_community.vectorstores import FAISS
from src.config import DB_DIRECTORY

from src.logger import get_logger

def create_vectorstore(chunks, embeddings):
    """
    Armazena chunks vetorizados no FAISS.

    Parameters:
        chunks (list): Lista de chunks.
        embedding: Modelo de embeddings.
        persist_directory (str): Diretório de armazenamento.

    Returns:
        Chroma: Banco vetorial criado.
    """
    logger = get_logger(__name__)
    
    # Remove diretório antigo, se necessário
    #if overwrite and os.path.exists(persist_directory):
    #    logger.warning(f"Removendo banco vetorial anterior em {persist_directory}")
    #    shutil.rmtree(persist_directory)

    logger.info("Criando novo banco vetorial em %s", DB_DIRECTORY)
    
    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    # Salvar o banco no disco
    vectorstore.save_local(folder_path=DB_DIRECTORY, index_name='index')
    logger.info("Banco vetorial salvo com sucesso. Total de documentos: %d", 
                vectorstore.index.ntotal)
    return vectorstore



def load_vectorstore(embedding):
    """
    Carrega o banco vetorial Chroma armazenado em disco.

    Parameters:
        persist_directory (str): Caminho onde o vetorstore foi salvo.
        embedding: Função de embedding usada na criação.

    Returns:
        Chroma: Banco vetorial carregado.
    """
    logger = get_logger(__name__)
    
    if not os.path.exists(DB_DIRECTORY):
        raise FileNotFoundError(f"Vector DB não encontrado em: {DB_DIRECTORY} ")
    else:
        vectorstore = FAISS.load_local(DB_DIRECTORY, embedding, 
                                       allow_dangerous_deserialization=True)
        logger.info('Banco de dados carregado com sucesso')
    return vectorstore

