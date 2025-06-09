"""logger.py file"""
import logging

def get_logger(name=__name__):
    """
    Cria e retorna um logger configurado com handlers para console e arquivo.

    Parâmetros:
    ----------
    name : str, opcional
        Nome do logger. Por padrão, usa o nome do módulo chamador (__name__).

    Funcionalidade:
    ---------------
    - Define o nível de logging como INFO.
    - Se o logger ainda não possuir handlers:
        - Configura saída de log para o console (stdout).
        - Configura saída de log para um arquivo chamado 'logfile.log'.
    - Usa codificação UTF-8.
    - Define o formato do log como: [data e hora]: mensagem.

    Retorna:
    -------
    logging.Logger
        Instância do logger configurado.
    """
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Se ainda não existir um log
    if not logger.handlers:
        logging.basicConfig(level=logging.INFO, 
                            encoding='utf-8', 
                            format= '[%(asctime)s]: %(message)s')
        logging.basicConfig(level=logging.INFO, 
                            filename='logfile.log', 
                            encoding='utf-8', 
                            format= '[%(asctime)s]: %(message)s')
    return logger
