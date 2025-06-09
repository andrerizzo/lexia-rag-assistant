"""retriever.py module."""
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from src.vectorstore import load_vectorstore
from src.embedder import embedder
from src.logger import get_logger


def rag_retriever(question):
    """
    Retriever
    """
    
    logger = get_logger(__name__)
    
    ## Criar primeiro prompt
    prompt_retriever_auxiliar = PromptTemplate(
        input_variables=["question"],
        template="""Você é um assistente jurídico especializado em LGPD. Sua tarefa é gerar cinco 
        versões diferentes da pergunta do usuário para recuperar documentos relevantes sobre LGPD 
        de uma base de dados vetorial. Gere perspectivas alternativas focadas em:
        1. Aspectos legais específicos
        2. Jurisprudência relacionada
        3. Direitos dos titulares
        4. Obrigações dos controladores
        5. Penalidades e sanções
        
        Forneça essas perguntas alternativas separadas por quebras de linha.
        Pergunta original: {question}""",
    )

    ## Definir o modelo
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(model='gpt-4o')

    ## Definir a chain
    query_generator_chain = prompt_retriever_auxiliar | llm | StrOutputParser()

    ## Carrega vectorstore
    embeddings = embedder()
    vectorstore = load_vectorstore(embeddings)

    ## Define document retriever
    doc_retriever = vectorstore.as_retriever()
     

    ## Gera prompt final para LLM
    system_prompt = """
        Você é um assistente jurídico especializado na Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018).

    INSTRUÇÕES PARA RESPOSTA:
    1. Use as informações disponíveis**: Trabalhe com as informações presentes nos documentos, mesmo que sejam parciais
    2. Seja útil: Forneça o máximo de informação relevante disponível nos documentos
    3. Contextualize: Explique conceitos jurídicos quando necessário
    4. Cite fontes: Quando possível, mencione artigos da LGPD ou referências jurisprudenciais
    5. Seja claro sobre limitações: Se algum aspecto específico não estiver detalhado, mencione isso, mas forneça o que está disponível

    IMPORTANTE: Os documentos podem conter informações fragmentadas. Use seu conhecimento jurídico para interpretar e conectar as informações de forma coerente.

    Apenas declare que a informação não está disponível se realmente NÃO houver NENHUMA informação relevante nos documentos fornecidos.

    CONTEXTO DOS DOCUMENTOS:
    {context}
    """

    prompt_retriever_final = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{question}")
    ])
    
    # Gera perguntas alternativas
    print("Gerando perguntas alternativas...")
    alternative_questions = query_generator_chain.invoke({"question": question})
    print(f"Perguntas geradas:\n{alternative_questions}\n")
    
    # 2. Separa as perguntas
    questions_list = alternative_questions.strip().split('\n')
    questions_list.append(question)  # Adiciona pergunta original
    
    # 3. Busca documentos para cada pergunta
    logger.info("Buscando documentos...")
    all_docs = []
    for i, q in enumerate(questions_list, 1):
        if q.strip():  # Ignora linhas vazias
            docs = doc_retriever.invoke(q.strip())
            all_docs.extend(docs)
            logger.info("Pergunta %d: %d documentos", i, len(docs))
    
    # Remove documentos repetidos
    unique_docs = []
    seen_content = set()
    for doc in all_docs:
        if doc.page_content not in seen_content:
            unique_docs.append(doc)
            seen_content.add(doc.page_content)
    
    logger.info("Total: %d documentos únicos", len(unique_docs))
        
    # Junta o conteúdo dos documentos
    context = "\n\n".join([doc.page_content for doc in unique_docs])

    # Monta o prompt e gera resposta
    final_chain = prompt_retriever_final | llm | StrOutputParser()
    logger.info("Chain final gerada com sucesso")
    response = final_chain.invoke({
        "context": context,
        "question": question,
    })
    logger.info("Resposta recebida do LLM")
    return response

