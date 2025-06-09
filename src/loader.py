""" loader.py """
import os
from datetime import datetime
from langchain_community.document_loaders import PyPDFLoader
from src.config import DATA_DIR
from src.logger import get_logger

def load_documents():
    """
    Carrega documentos PDF de um diretório para uso em um pipeline 
    RAG (Retrieval-Augmented Generation).

    Esta função percorre recursivamente o diretório especificado, 
    identifica arquivos PDF, carrega seu conteúdo usando o PyPDFLoader 
    e adiciona metadados úteis, como caminho do arquivo, nome, tipo, 
    identificador único e data de ingestão.

    Parameters:
        datadir (str): Caminho do diretório onde os arquivos PDF estão 
        armazenados.

    Returns:
        list: Lista de documentos carregados com metadados, prontos 
        para processamento em um sistema RAG.
    """
    logger = get_logger(__name__)
    docs = []

    ### Carrega arquivos
    for root, _,files in os.walk(DATA_DIR):
        for file in files:
            filepath= os.path.join(root, file)
            if os.path.isfile(filepath):
                if file.lower().endswith("pdf"):
                    ## Trata arquivos PDF
                    ext = 'pdf'
                    loader=PyPDFLoader(filepath)
                    loaded_doc = loader.load()
                    ## Adição de metadados
                    for d in loaded_doc:
                        d.metadata.update({
                            "source": filepath,
                            "filename": os.path.basename(filepath),
                            "filetype": ext,
                            "ingest_date": datetime.now().isoformat()
                    })
                    ## Gera lista com os documentos carregados
                    docs.extend(loaded_doc)
                    logger.info("Arquivo carregado com sucesso: %s", file)
    logger.info("Todos os documentos foram carregados com sucesso")
    return docs
