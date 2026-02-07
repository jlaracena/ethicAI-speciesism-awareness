# 🌿 ethicAI-speciesism-awareness: Espejo de Conciencia

Un Tutor Socrático diseñado para guiar a los usuarios a través de una autorreflexión profunda sobre el especismo y nuestra relación con los demás animales sintientes.

## 🌟 Visión
No es un chatbot convencional. Es una experiencia de diálogo que utiliza una **máquina de estados** para confrontar nuestras premisas éticas con nuestras conductas cotidianas, utilizando datos científicos de sintiencia como base.

## 🛠️ Arquitectura
- **Backend**: FastAPI (Python) - Gestiona la lógica de la máquina de estados y las contradicciones éticas.
- **Frontend**: Streamlit - Interfaz Zen y minimalista diseñada para la reflexión.
- **Base de Conocimientos**: Datos científicos sobre la inteligencia y emoción animal.

## 🚀 Cómo empezar

### 1. Instalación de Dependencias
Asegúrate de tener Python instalado y ejecuta:
```bash
pip install fastapi uvicorn streamlit requests
```

### 2. Ejecución del Proyecto
Para ver el frontend, necesitas ejecutar **ambos** servicios en terminales separadas:

**Terminal 1 (Backend):**
```bash
uvicorn backend.main:app --reload
```

**Terminal 2 (Frontend):**
```bash
streamlit run frontend/app.py
```

El navegador se abrirá automáticamente en `http://localhost:8501`.

## 🧠 Flujo Socrático
El bot te guiará a través de cuatro etapas clave:
1. **Empatía**: Conexión emocional con el sentir animal.
2. **Criterio**: Definición de un estándar moral compartido.
3. **Disonancia (El Espejo)**: Observación de la brecha entre valores y acciones.
4. **Resolución**: Integración consciente y hechos de sintiencia.

---
*Desarrollado con ❤️ para el ecosistema ethicAI.*
