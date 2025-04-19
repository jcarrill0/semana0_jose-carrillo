# Importar las librerías necesarias
from  fastapi import  FastAPI
from  pydantic import  BaseModel
from  dotenv import  load_dotenv
import  os
import ollama

# Cargar variables de entorno desde el archivo .env
load_dotenv()
# Crear una instancia de FastAPI
app = FastAPI()

# Modelo de datos para recibir la pregunta 
class  Pregunta(BaseModel):
    texto: str

# Endpoint para recibir preguntas y devolver respuestas
@app.post("/preguntar")
async  def  preguntar(pregunta: Pregunta):
    # Aquí llamarías al modelo de IA para obtener una respuesta 
    respuesta = ollama.chat(model="deepseek-r1", messages=[{"role": "user", "content":pregunta.texto}])
    #respuesta = "Esta es una respuesta simulada para: " + pregunta.texto 
    return {"respuesta": respuesta["message"]["content"]} #{"respuesta": respuesta}