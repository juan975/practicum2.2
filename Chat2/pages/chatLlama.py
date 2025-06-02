import streamlit as st
from ollama import chat

def chat_with_llama_stream(prompt):
    # Instrucción contextual para dirigir al modelo
    contexto = (
        "Eres un modelo de lenguaje experto en clasificación de texto. "
        "Tu tarea es leer un texto y responder únicamente con su categoría correspondiente. "
        "Algunas categorías comunes incluyen: política, tecnología, ciencia, arte, deportes, educación, negocios, entretenimiento o salud. "
        "No expliques tu respuesta, solo responde con la categoría más adecuada.\n\n"
    )

    mensaje_usuario = contexto + prompt

    # Streaming desde el modelo llama
    stream = chat(
        model="llama3",
        messages=[{"role": "user", "content": mensaje_usuario}],
        stream=True,
    )

    respuesta_completa = ""
    contenedor = st.empty()  # Contenedor actualizable

    for chunk in stream:
        respuesta_completa += chunk['message']['content']
        contenedor.markdown(f"**Asistente:** {respuesta_completa}")

    return respuesta_completa


# Interfaz en Streamlit
st.title("Asistente con LLaMA")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Tú:", key="input")

if st.button("Enviar") and user_input:
    with st.spinner("Pensando..."):
        respuesta = chat_with_llama_stream(user_input)
        st.session_state.history.append(("Tú", user_input))
        st.session_state.history.append(("Asistente", respuesta))

# Mostrar conversación en orden descendente (lo más reciente arriba)
for quien, texto in reversed(st.session_state.history):
    st.markdown(f"**{quien}:** {texto}")
