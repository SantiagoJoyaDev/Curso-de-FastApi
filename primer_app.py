from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Esto es una instancia de FastAPI
app = FastAPI() # Esta linea crea la instancia de la clase FastAPI.
app.title = "mi aplicacion con FastAPI"# Se le asigna un titulo a la aplicacion.
app.version = "3.1.0" # Se le asigna una version a la aplicacion.

# Esto es un decorador, se usa para indicar que la siguiente funcion es un manejador de peticiones.
@app.get("/",tags=["Home"])
# Esta funcion se ejecuta cuando se recibe una peticion GET a la raiz de la aplicacion.
def get_home():# Esto es un decorador, se usa para indicar que la siguiente funcion es un manejador de peticiones.
    # Esto es un diccionario, se usa para enviar datos a la aplicacion.
    return {"Hello": "World"}

@app.get("/home2",tags=["Home"])
def get_home2():
    return {"Hello": "World"}
    
@app.get("/home3",tags=["Home"])
def get_home3():
    return HTMLResponse('<h1>Respuesta desde HTML --> Santiago Joya </h1>')
#Movies
movies = [ #Listado de peliculas en formato de diccionario. 
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": 2009,
        "rating": 7.8,
        "category": "Accion"
    },
    {
        "id": 2,
        "title": "Avatar 2",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": 2022,
        "rating": 7.8,
        "category": "Accion"
    },
    {
        "id": 3,
        "title": "Avatar 3",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": 2023,
        "rating": 7.8,
        "category": "Accion"
    },
    {
        "id": 4,
        "title": "Los locos adams",
        "overview": " risas risas y mas risas",
        "year": 2019,
        "rating": 9.0,
        "category": "Comedia"
    }
]

@app.get("/movies",tags=["Movies"])
def get_movies():
    return {"message":"Here is the list of movies."}

@app.get("/movies2",tags=["Movies"])
def get_movies2():
    return {"message":"Here is the list of movies."}

@app.get("/movies3",tags=["Movies"])
def get_movies3():
    return movies

@app.get("/movies4/{id}",tags=["Movies"])# con parametro de ruta
def get_movie4(id:int):
    return id

@app.get("/movies5/{id}",tags=["Movies"])# con parametro de ruta y validación de datos
def get_movie5(id:int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return {"message":"Movie not found"}

@app.get("/movies6/",tags=["Movies"])# con parametro de ruta por categoria
def get_movie6(category:str,year:int):#(Aqui se cargan mas datos a esta ruta, son obligatorios)
    for movie in movies:
        if movie["category"] == category and movie["year"] == year:
            return movie
    return {"message":"Movie not found"}

#Cars
@app.get("/cars",tags=["Cars"])
def get_cars():
    return {"message":"Here is the list of cars."}