import streamlit as st
import requests

st.title("Auxiliar Jurídico para LGPD")

# Campo para pergunta
question = st.text_area("Em que posso te ajudar?")

# Função que faz POST na API
def generate_response(question):
    """Envia pergunta para a API FastAPI"""
    url = "http://localhost:8000/rag"  # Endpoint da API
    payload = {"question": question}
    try:
        response = requests.post(url, json=payload, timeout=120)
        if response.status_code == 200:
            return response.json().get("response", "Sem resposta retornada.")
        else:
            return f"Erro: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Erro de conexão com a API: {str(e)}"

# Formulário
if st.button("Enviar"):
    if question:
        resposta = generate_response(question)
        st.write("**Resposta:**")
        st.markdown(resposta)
    else:
        st.warning("Por favor, escreva uma pergunta.")
