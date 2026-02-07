from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
import json

app = FastAPI(title="ethicAI-speciesism-awareness")

# Load knowledge base
with open("knowledge_base.json", "r") as f:
    knowledge_base = json.load(f)

class UserInput(BaseModel):
    state: str
    response: str
    history: List[Dict[str, str]] = []

class BotResponse(BaseModel):
    next_state: str
    message: str
    options: List[str]
    evidence: Optional[str] = None

STATES = {
    "START": {
        "message": "Bienvenido. ¿Crees que los animales son capaces de sentir dolor o alegría?",
        "options": ["Sí, lo creo", "No estoy seguro", "No lo creo"],
        "next": "EMPATHY"
    },
    "EMPATHY": {
        "positive": "CRITERIA",
        "negative": "REASONING" # Simple state for those who doubt sentience
    },
    "CRITERIA": {
        "message": "Si aceptamos que sienten, ¿crees que es correcto causarles dolor innecesario?",
        "options": ["No, no es correcto", "A veces es necesario"],
        "next": "DISSONANCE"
    },
    "DISSONANCE": {
        "message": "Mencionas que no es correcto causar dolor innecesario. Sin embargo, el consumo de carne suele implicar ese dolor y no es una necesidad biológica hoy en día. ¿Cómo concilias esto?",
        "options": ["Es la cadena alimenticia", "Es por necesidad", "No lo había pensado"],
        "next": "RESOLUTION"
    }
}

def get_socratic_response(state: str, response: str) -> BotResponse:
    if state == "START":
        return BotResponse(
            next_state="EMPATHY",
            message="Si los animales sienten, ¿qué crees que nos obliga moralmente hacia ellos?",
            options=["Respetar su vida", "No hacerles daño", "Nada en especial"]
        )
    
    if state == "EMPATHY":
        return BotResponse(
            next_state="CRITERIA",
            message="Has mencionado que valoras el bienestar animal. ¿Estarías de acuerdo con este principio: 'No debemos causar sufrimiento innecesario'?",
            options=["Totalmente de acuerdo", "Depende de la especie", "No estoy de acuerdo"]
        )
    
    if state == "CRITERIA":
        return BotResponse(
            next_state="DISSONANCE",
            message="Si estamos de acuerdo en no causar dolor innecesario... ¿Cómo ves el hecho de que consumimos productos que requieren ese dolor, teniendo alternativas?",
            options=["Es una contradicción", "Es por tradición", "Es por salud"]
        )
    
    if state == "DISSONANCE":
        evidence = ""
        msg = "¿Por qué crees que eso justifica el dolor?"
        if "cadena" in response.lower():
            evidence = knowledge_base["falacias_especistas"]["cadena_alimenticia"]
        elif "necesidad" in response.lower() or "salud" in response.lower():
            evidence = knowledge_base["falacias_especistas"]["necesidad_biologica"]
        
        # Integration of sentience facts
        fact = knowledge_base["sentiencia_facts"][0] # Example for pigs
        fact_msg = f"Dato: Sabías que los {fact['especie']}s tienen una {fact['atributo']} tal que {fact['dato']}"
        
        return BotResponse(
            next_state="RESOLUTION",
            message=f"Entiendo. {evidence or msg} Reflexionemos sobre esto: {fact_msg}",
            options=["Deseo profundizar", "Cerrar sesión"],
            evidence=evidence
        )

    return BotResponse(
        next_state="START",
        message="¿Reiniciamos nuestro diálogo?",
        options=["Sí", "No"]
    )

@app.post("/evaluate", response_model=BotResponse)
async def evaluate(user_input: UserInput):
    return get_socratic_response(user_input.state, user_input.response)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
