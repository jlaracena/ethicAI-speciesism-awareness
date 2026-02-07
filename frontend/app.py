import streamlit as st
import requests
import base64

# Page Configuration
st.set_page_config(
    page_title="ethicAI - Socratic Tutor", 
    page_icon="🌿", 
    layout="wide", # Wider layout for better background visibility
    initial_sidebar_state="expanded"
)

# Session State Initialization
if "current_state" not in st.session_state:
    st.session_state.current_state = "START"
if "message" not in st.session_state:
    st.session_state.message = "Bienvenido a un espacio de reflexión. ¿Crees que los animales son capaces de experimentar sensaciones como nosotros (dolor, alegría, miedo)?"
if "options" not in st.session_state:
    st.session_state.options = ["Sí, lo creo", "No estoy seguro", "No lo creo"]
if "history" not in st.session_state:
    st.session_state.history = []

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(bin_file):
    try:
        bin_str = get_base64_of_bin_file(bin_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.02), rgba(0, 0, 0, 0.02)), url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-position: center 85%; /* Ensures animals at the bottom are visible */
            background-attachment: fixed;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except:
        pass

# Force Background
set_png_as_page_bg("frontend/assets/background.png")

# Zen Custom CSS with Glassmorphism
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Outfit', sans-serif;
    }

    /* Hide standard backgrounds */
    .stApp {
        background-color: transparent;
    }

    /* Primary color override */
    :root {
        --primary-color: #2d5a27;
    }

    /* Sidebar - Beautifully styled */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 252, 240, 0.6) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(220, 200, 150, 0.3);
    }
    
    [data-testid="stSidebar"] div.stMarkdown, 
    [data-testid="stSidebar"] div.stAlert {
        border-radius: 20px;
        background-color: rgba(255, 255, 255, 0.75) !important;
        border: 1px solid rgba(220, 200, 150, 0.4);
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    [data-testid="stSidebar"] * {
        color: #3d2b1f !important;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 40px;
        background-color: rgba(255, 255, 255, 0.95);
        color: #1e3a1e;
        border: 1px solid rgba(255, 255, 255, 0.5);
        padding: 18px 25px;
        font-size: 1.1rem;
        font-weight: 500;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }

    .stButton>button:hover {
        background-color: #2d5a27;
        color: white;
        border: 1px solid #2d5a27;
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(45, 90, 39, 0.2);
    }

    /* Typography */
    .bot-header {
        color: #ffffff;
        font-weight: 600;
        font-size: 4.5rem;
        letter-spacing: -2px;
        text-align: left;
        padding-top: 80px;
        margin-bottom: 0;
        text-shadow: 0 4px 20px rgba(0,0,0,0.6);
    }
    
    .bot-subheader {
        color: rgba(255,255,255,1);
        font-size: 1.6rem;
        font-weight: 300;
        text-align: left;
        margin-top: 0;
        margin-bottom: 80px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.4);
    }

    /* Content Box */
    .chat-bubble {
        background: rgba(255, 255, 255, 0.96);
        backdrop-filter: blur(20px);
        padding: 50px;
        border-radius: 35px;
        border: 1px solid rgba(255, 255, 255, 0.6);
        box-shadow: 0 25px 60px rgba(0,0,0,0.18);
        margin-bottom: 50px;
        color: #0d1a0d;
        font-size: 1.7rem;
        font-weight: 400;
        line-height: 1.7;
        text-align: left;
        animation: slideUp 1.2s ease-out;
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Progress Dots */
    .progress-container {
        display: flex;
        justify-content: flex-start;
        gap: 15px;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    .progress-dot {
        width: 12px;
        height: 12px;
        background: rgba(255,255,255,0.3);
        border-radius: 50%;
        transition: all 0.6s ease;
    }
    .progress-dot.active {
        background: #ffffff;
        box-shadow: 0 0 15px rgba(255,255,255,1);
        transform: scale(1.3);
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* Center layout helper */
    [data-testid="column"] {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Socratic Progress
stages = ["START", "EMPATHY", "CRITERIA", "DISSONANCE", "RESOLUTION"]
current_idx = stages.index(st.session_state.current_state) if st.session_state.current_state in stages else 0

# Progress UI
progress_html = "<div class='progress-container'>"
for i in range(len(stages)):
    active_class = "active" if i <= current_idx else ""
    progress_html += f"<div class='progress-dot {active_class}'></div>"
progress_html += "</div>"
st.markdown(progress_html, unsafe_allow_html=True)

st.markdown("<h1 class='bot-header'>ethicAI</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='bot-subheader'>Espejo de Conciencia: Un viaje socrático</h2>", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 🌱 Tu Diálogo")
if st.session_state.history:
    for entry in st.session_state.history:
        st.sidebar.markdown(f"**Tú:** {entry['user']}")
        st.sidebar.markdown(f"**Guía:** {entry['bot'][:100]}...")
        st.sidebar.markdown("---")
else:
    st.sidebar.markdown("Bienvenido. Aquí broten las semillas de nuestra reflexión.")

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

# Main Layout
col1, col2 = st.columns([0.6, 0.4])

with col1:
    st.markdown(f"<div class='chat-bubble'>{st.session_state.message}</div>", unsafe_allow_html=True)
    
    # Elegant Buttons
    btn_cols = st.columns(len(st.session_state.options))
    for i, option in enumerate(st.session_state.options):
        if btn_cols[i].button(option, key=f"btn_{option}_{st.session_state.current_state}"):
            send_response(option)
            st.rerun()

st.sidebar.markdown("---")
st.sidebar.info("Tutor socrático para la toma de conciencia sobre el especismo.")
