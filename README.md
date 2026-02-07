# 🌿 ethicAI-speciesism-awareness: Espejo de Conciencia

[![Deployed on Cloud Run](https://img.shields.io/badge/Deployed%20on-Cloud%20Run-blue?logo=google-cloud&logoColor=white)](https://console.cloud.google.com/run)
[![Project: ethicAI](https://img.shields.io/badge/Project-ethicAI-green)](https://github.com/topics/ethicai)

Un **Tutor Socrático** de última generación diseñado para guiar a los usuarios a través de una autorreflexión profunda sobre el especismo y nuestra relación con los demás animales sintientes. Inspirado en la mayéutica, este bot no juzga: pregunta para que tú mismo descubras tus propias contradicciones.

---

## 🌟 Visión del Proyecto
En un mundo donde la desconexión con el origen de nuestro consumo es la norma, **ethicAI** actúa como un puente de consciencia. Utilizando una máquina de estados lógica y datos científicos sobre la sintiencia animal, el tutor guía al usuario desde la empatía básica hasta la resolución ética.

## 🚀 Características Principales
- **🧩 Lógica Socrática**: Máquina de estados (Empatía -> Criterio -> Disonancia -> Resolución) que guía el diálogo sin confrontación.
- **📚 Base de Conocimiento**: Integración de hechos científicos sobre la sintiencia de cerdos, vacas y otros animales.
- **🎨 Interfaz Zen**: Diseño minimalista, natural y reflexivo en Streamlit con efectos de glassmorphism.
- **🐳 Cloud Ready**: Contenerizado con Docker para despliegue inmediato en Cloud Run.

## 🛠️ Stack Tecnológico
- **Backend**: FastAPI (Python)
- **Frontend**: Streamlit (Zen Custom CSS)
- **Despliegue**: Docker + Google Cloud Run
- **Estilo**: Outfit (Google Fonts)

## 📸 Demo Visual
*(Aquí se incluiría un GIF de la interfaz Zen)*
![Preview](frontend/assets/background.png)

## 📥 Instalación y Uso Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/[USUARIO]/ethicAI-speciesism-awareness.git
   cd ethicAI-speciesism-awareness
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar Localmente:**
   - **Backend**: `uvicorn backend.main:app --reload`
   - **Frontend**: `streamlit run frontend/app.py`

## ☁️ Despliegue en la Nube
El proyecto está optimizado para **Google Cloud Run**.
```bash
gcloud run deploy --source .
```

---

## 🤝 Contribuir
Este es un proyecto de código abierto parte de la iniciativa **ethicAI-hub**. Las contribuciones que promuevan la reflexión ética son bienvenidas.

---

**Desarrollado con ❤️ por Jinshi (antigravity) para ethicAI-hub.**
