import streamlit as st
import requests

st.set_page_config(page_title="ethicAI - Socratic Tutor", page_icon="🌿", layout="centered")

# Zen Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f1;
        color: #2c3e50;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #ffffff;
        color: #2c3e50;
        border: 1px solid #d1d8e0;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #2c3e50;
        color: #ffffff;
        border: 1px solid #2c3e50;
    }
    .bot-header {
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        letter-spacing: 1px;
        text-align: center;
        padding-bottom: 20px;
    }
    .chat-bubble {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='bot-header'>🌿 ethicAI: Espejo de Conciencia</h1>", unsafe_allow_html=True)

# Session State
if "current_state" not in st.session_state:
    st.session_state.current_state = "START"
if "message" not in st.session_state:
    st.session_state.message = "Bienvenido a un espacio de reflexión. ¿Crees que los animales son capaces de experimentar sensaciones como nosotros (dolor, alegría, miedo)?"
if "options" not in st.session_state:
    st.session_state.options = ["Sí, lo creo", "No estoy seguro", "No lo creo"]
if "history" not in st.session_state:
    st.session_state.history = []

def send_response(option):
    try:
        resp = requests.post("http://localhost:8000/evaluate", json={
            "state": st.session_state.current_state,
            "response": option,
            "history": st.session_state.history
        })
        data = resp.json()
        
        st.session_state.history.append({"user": option, "bot": data["message"]})
        st.session_state.current_state = data["next_state"]
        st.session_state.message = data["message"]
        st.session_state.options = data["options"]
        
    except Exception as e:
        st.error(f"Error de conexión con el backend: {e}")

# UI layout
st.markdown(f"<div class='chat-bubble'>{st.session_state.message}</div>", unsafe_allow_html=True)

cols = st.columns(len(st.session_state.options))
for i, option in enumerate(st.session_state.options):
    if cols[i].button(option):
        send_response(option)
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.info("Este tutor socrático te guía a través de un diálogo reflexivo sobre nuestra relación con otras especies.")
