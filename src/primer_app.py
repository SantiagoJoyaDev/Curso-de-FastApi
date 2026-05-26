from fastapi import FastAPI, Path, Query, Body
from src.routers.movie_router import movie_router
from src.routers.user_router import user_router

from src.routers.review_router import review_router
# "Body" se usa con el metodo numero 1 de obtener datos de la peticion, y "BaseModel" con el metodo numero 2 de obtener datos de la peticion
# El body es para recibir datos de la peticion, y el path es para recibir datos de la ruta
from fastapi.responses import (
    HTMLResponse,
    JSONResponse,
    PlainTextResponse,
    RedirectResponse,
    FileResponse,
)
from pydantic import BaseModel, Field, validator  # Forma 2 de realizarlo(Schemas)
from typing import (
    Optional,
    List,
)  # El Optinal es para el metodo 2 de la clase Movie, y List es para el metodo 2 de la clase Movie
import datetime

# Configuración de la aplicación
app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "1.0.0"

# --- RUTAS DE LA APLICACIÓN ---

@app.get("/", tags=["Home"])
def get_home():
    return HTMLResponse("<h1>Respuesta desde FastAPI</h1>")
    # Otra manera de hacerlo es: return PlainTextResponse('<h1>Respuesta desde FastAPI</h1>')

app.include_router(prefix="/movies",router=movie_router)
app.include_router(prefix="/users",router=user_router)
app.include_router(prefix="/reviews",router=review_router)

# --- OTRAS SECCIONES (Práctica) ---

@app.get("/community", tags=["Community"])
def get_community():
    return {"message": "Comunidad de películas."}

@app.get("/image", tags=["Image"])
def get_image():
    return FileResponse("image.jpg")