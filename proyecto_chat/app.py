from flask import Flask, request, jsonify, send_from_directory
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Cargar API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Funciones para cargar archivos
def cargar_horarios():
    horarios = {}
    with open("horarios.txt", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): 
                continue
            dia, clase = line.strip().split("|", 1)
            dia = dia.lower()
            horarios.setdefault(dia, []).append(clase)
    return horarios

def cargar_examenes():
    examenes = {}
    with open("examenes.txt", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): 
                continue
            materia, fecha = line.strip().split("|", 1)
            examenes[materia.lower()] = fecha
    return examenes

HORARIOS = cargar_horarios()
EXAMENES = cargar_examenes()

# Rutas
@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/style.css")
def css():
    return send_from_directory('.', 'style.css')

@app.route("/script.js")
def js():
    return send_from_directory('.', 'script.js')

@app.route("/consulta", methods=["POST"])
def consulta():
    data = request.get_json()
    mensaje = data.get("mensaje", "").lower()

    # Buscar horarios
    if "que tengo" in mensaje:
        for dia in HORARIOS:
            if dia in mensaje:
                clases = HORARIOS[dia]
                return jsonify({"respuesta": f"{dia.capitalize()}: " + ", ".join(clases)})
        return jsonify({"respuesta": "No encontré clases para ese día."})

    # Buscar exámenes
    if "examen" in mensaje:
        for materia in EXAMENES:
            if materia in mensaje:
                return jsonify({"respuesta": f"Examen encontrado: {EXAMENES[materia]}"})
        return jsonify({"respuesta": "No encontré información para esa consulta."})

    return jsonify({"respuesta": "No entendí tu consulta."})

if __name__ == "__main__":
    app.run(debug=True)
