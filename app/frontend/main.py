import streamlit as st
import requests

st.set_page_config(page_title="LexIA - Auxiliar Jurídica LGPD")
st.title("💼 LexIA — Auxiliar Jurídico para LGPD")

# Inicializa histórico de conversa (uma vez por sessão)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Função para enviar pergunta para a API
def generate_response(question):
    url = "http://localhost:8000/rag"  # endpoint da API FastAPI
    payload = {"question": question}
    try:
        response = requests.post(url, json=payload, timeout=120)
        if response.status_code == 200:
            return response.json().get("response", "Sem resposta retornada.")
        else:
            return f"Erro {response.status_code}: {response.text}"
    except Exception as e:
        return f"Erro de conexão com a API: {str(e)}"

# Exibe histórico do chat
for user_msg, bot_msg in st.session_state.chat_history:
    with st.chat_message("user", avatar="🧑‍⚖️"):
        st.markdown(user_msg)
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(bot_msg)

# Entrada de nova pergunta
question = st.chat_input("Digite sua pergunta sobre a LGPD...")

if question:
    with st.chat_message("user", avatar="🧑‍⚖️"):
        st.markdown(question)

    # Mostra uma "mensagem de espera" enquanto processa
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Consultando base jurídica e gerando resposta..."):
            resposta = generate_response(question)
            st.markdown(resposta)

    # Salva pergunta e resposta no histórico
    st.session_state.chat_history.append((question, resposta))

