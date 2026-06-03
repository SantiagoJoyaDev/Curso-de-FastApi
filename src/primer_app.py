from fastapi import FastAPI, Path, Query, Body, Depends
from fastapi import Request
from fastapi.responses import Response
from src.routers.movie_router import movie_router
from src.routers.user_router import user_router
from src.routers.review_router import review_router
from src.utilities.http_error_handler import HTTPErrorHandler
from typing import Annotated
#Importacion de Jinja2Templates y StaticFiles para manejar archivos estaticos y plantillas
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
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
#Esto es para manejar las dependencias globales, se ejecuta antes de cada peticion
def dependency1():
    print("Globlal dependency 1")

def dependency2():
    print("Global dependency 2")

# Configuración de la aplicación
app = FastAPI(dependencies=[Depends(dependency1), Depends(dependency2)])
app.title = "Mi aplicación con FastAPI"
app.version = "1.0.0"
#app.add_middleware(HTTPErrorHandler)
@app.middleware("http")#Middleware de tipo http, me permite ejecutar código antes y después de cada petición este es un middleware usando ya FastAPI 
async def http_error_handler(request:Request, call_next) -> Response | JSONResponse:
    print("Middleware ejecutado")       
    return await call_next(request)#Lo que hace el call_next es llamar a la función que sigue en la cadena de middlewares, o en este caso, a la función que maneja la petición

#Configuracion de archivos estaticos y plantillas
static_path = os.path.join(os.path.dirname(__file__), "static") 
templates_path = os.path.join(os.path.dirname(__file__), "templates")

app.mount("/static", StaticFiles(directory=static_path), name="static")
templates = Jinja2Templates(directory=templates_path)

# --- RUTAS DE LA APLICACIÓN ---
@app.get("/", tags=["Home"])
def get_home(request:Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"request": request, "title": "Welcome to FastAPI"})
    #Otra manera de hacerlo es: HTMLResponse("<h1>Respuesta desde FastAPI</h1>")
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


#Practica de inyeccion de dependencias
#Creacion de la dependencia mediante una funcion
# def common_parameters(start_date: str, end_date: str):
#     return {"start_date": start_date, "end_date": end_date}

# Para no repetir codigo en los parametros podemos inicializar una funcion la cual reciba los parametros y los devuelva
# commonDep = Annotated[dict, Depends(common_parameters)] #Usamos Annotated para declarar la dependencia
#Para users y customers hicimos la declaracion de dependencias mediante annotated, con el cual pudimos evitar tener que hacer
#dos imports, una importacion para la dependencia y otra importacion para el Query (country:Annotated[str, Query(max_length=20)],)

#Creacion de la dependencia mediante una clase
class CommonDep:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

@app.get("/users")
def get_users(commons:CommonDep = Depends()):
    return f"Users creted between {commons.start_date} and {commons.end_date}"

@app.get("/customers")
def get_costumers(commons:CommonDep = Depends()):#Borramos el CommonDep al final para que se muestre de una manera mas limpia y clara la documentacion ya que cuando
    #se llaman igual no es necesario poner el nombre de la funcion en el Depends ya que Python lo puede inferir automaticamente
    return f"Users creted between {commons.start_date} and {commons.end_date}"