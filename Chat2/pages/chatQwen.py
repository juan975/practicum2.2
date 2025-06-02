import streamlit as st
import requests

def chat_with_qwen(prompt):
    # Instrucción contextual para dirigir al modelo
    contexto = (
        "Eres un asistente experto en arquitectura. "
        "Responde de forma clara, precisa y profesional "
        "cualquier pregunta relacionada con diseño arquitectónico, estructuras, urbanismo, materiales de construcción, normas técnicas, sostenibilidad, historia de la arquitectura y gestión de proyectos.\n\n"
    )

    prompt_modificado = contexto + prompt
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "qwen", "prompt": prompt_modificado, "stream": False}
    )
    return response.json()["response"]


st.title("Asistente con Qwen")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Tú:", key="input")

if st.button("Enviar") and user_input:
    with st.spinner("Pensando..."):
        respuesta = chat_with_qwen(user_input)
        st.session_state.history.append(("Asistente", respuesta))
    st.session_state.history.append(("Tú", user_input))

# Mostrar conversación
for quien, texto in reversed(st.session_state.history):
    st.markdown(f"**{quien}:** {texto}")
