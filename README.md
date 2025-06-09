
# ⚖️LexIA — Assistente Jurídico com RAG para LGPD

**LexIA** (Lex = Lei + IA) é um assistente jurídico inteligente baseado em **RAG** (_Retrieval-Augmented Generation_), desenvolvido para responder perguntas sobre a **Lei Geral de Proteção de Dados (LGPD)** utilizando documentos legais, pareceres e jurisprudências vetorizadas.

## 🎯 Visão Geral

O LexIA combina técnicas de **NLP**, **recuperação semântica** e **LLMs** para fornecer respostas claras, contextualizadas e juridicamente embasadas, tornando o conhecimento legal mais acessível e confiável.

## ✨ Principais Funcionalidades

- 🔍 **Busca Semântica Avançada**: Vetorização via embeddings para recuperação de documentos relevantes
- 💬 **Respostas Contextualizadas**: Geração baseada nos documentos recuperados
- ⚖️ **Base Legal Confiável**: Fontes oficiais (LGPD, STJ, ANPD)
- 🧑‍💼 **Interface Intuitiva**: Front-end interativo com Streamlit
- 📊 **Observabilidade**: Integração com LangSmith
- 🐳 **Deploy Simplificado**: Containerização com Docker

## 🏗️ Arquitetura Técnica

```plaintext

┌──────────────┐    ┌───────────────┐    ┌──────────────┐
│  Streamlit   │ ◄► │   FastAPI     │ ◄► │   FAISS DB   │
│  Frontend    │    │   Backend     │    │ Vector Store │
└──────────────┘    └───────────────┘    └──────────────┘
                          │                    │
                          ▼                    ▼
               ┌──────────────────┐   ┌──────────────────┐
               │    LangChain     │   │   Hugging Face   │
               │   Pipeline RAG   │   │    Embeddings    │
               └──────────────────┘   └──────────────────┘
                          │
                          ▼
                  ┌─────────────┐
                  │   GPT-4o    │
                  │   OpenAI    │
                  └─────────────┘

```

## 🛠️ Stack Tecnológica

**RAG Core:**

- LangChain
- GPT-4o (OpenAI)
- Hugging Face Embeddings
- FAISS

**Backend & API:**

- FastAPI
- Python 3.12
- Poetry

**Frontend:**

- Streamlit
- Requests

**Deploy & Monitoramento:**

- Docker + Docker Compose
- LangSmith (debug/observabilidade)

## 📚 Base de Conhecimento

A aplicação processa e indexa:

- 📋 Lei nº 13.709/2018 (LGPD) — texto integral
- ⚖️ Jurisprudência do STJ — decisões relevantes
- 📄 Guias e notas da ANPD
- 🔗 Legislação complementar correlata

## 🚀 Instalação e Execução

### ✅ Pré-requisitos

- Python 3.12+
- Docker e Docker Compose
- Chave da OpenAI (API Key)

### 💻 Instalação Local

```bash

gitclonehttps://github.com/seu-usuario/lexia-rag-assistant.git

cdlexia-rag-assistant

cp.env.example.env

poetryinstall

poetryshell

uvicornapp.backend.api:app--port8000

# Em outro terminal:

streamlitrunapp.frontend.main.py--server.port8501

```

### 🐳 Deploy com Docker (Recomendado)

```bash

docker-composeup-d

# Frontend → http://localhost:8501

# API → http://localhost:8000

```

## 💡 Exemplos de Uso

### ✔️ Via Interface Web

**Pergunta:** “Quais são os direitos do titular segundo a LGPD?”

**Resposta:** “De acordo com o Art. 18 da LGPD, o titular tem direito a obter do controlador...”

### ✔️ Via API REST

```bash

curl-XPOSThttp://localhost:8000/rag\

     -H "Content-Type: application/json" \

     -d'{"question": "O que é dado pessoal sensível?"}'

```

## 🔮 Roadmap

- ☁️ Deploy em Nuvem (ECS / GCP / Render)
- 📚 Expansão para outras áreas do Direito
- 📑 Exportação de respostas em PDF

## 📞 Contato

**André Rizzo — Cientista de Dados Sênior**
📧 andrerizzo@gmail.com
💼 LinkedIn: https://linkedin.com/in/andrerizzo1
🐙 GitHub: https://github.com/andrerizzo
