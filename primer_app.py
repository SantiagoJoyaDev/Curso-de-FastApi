from fastapi import FastAPI
# "Body" se usa con el metodo numero 1 de obtener datos de la peticion, y "BaseModel" con el metodo numero 2 de obtener datos de la peticion
# El body es para recibir datos de la peticion, y el path es para recibir datos de la ruta
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field  #Forma 2 de realizarlo(Schemas)
from typing import Optional, List #El Optinal es para el metodo 2 de la clase Movie, y List es para el metodo 2 de la clase Movie
import datetime

# Configuración de la aplicación
app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "1.0.0"

#MODELOS o SCHEMAS
# Definición del Modelo de Datos (Esquema de la Película) Forma 2 de realizarlo(Schemas)
class Movie(BaseModel):
    #id: Optional[int] = None Forma 2 de realizarlo
    #Otra manera de hacerlo es poner : int | None = None
    id: int
    title: str 
    overview: str
    year: int
    rating: float
    category: str

class CreateMovie(BaseModel):#Validaciones con Field
    id: int 
    title: str = Field(min_length=5, max_length=15, default= "titulo por defecto")
    overview: str = Field(min_length=5, max_length=50, default= "descripcion por defecto")
    year: int = Field(le=datetime.datetime.now().year, default= 2024) #otra manera de hacerlo Field(ge=1800, le=2023)
    rating: float = Field(ge=0, le=10, default= 0)
    category: str = Field(min_length=5, max_length=50, default= "categoria por defecto")
    #gt es mayor que, lt es menor que, ge es mayor o igual que, le es menor o igual que
    #ge 1800 y le 2023, significa que el año debe ser mayor o igual a 1800 y menor o igual a 2023
    #lt 0 y ge 10, significa que la calificacion debe ser menor que 0 y mayor o igual a 10
    #le 50, significa que la categoria debe ser menor o igual a 50
    #le datetime.datetime.now().year, significa que el año debe ser menor o igual al año actual

    model_config = {#Esto es para la documentacion de swagger y obtener ejemplos osea para que se muestre el ejemplo al momento de crear la pelicula
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Avatar",
                    "overview": "En un exuberante planeta llamado Pandora viven los Na'vi...",
                    "year": 2009,
                    "rating": 7.8,
                    "category": "Acción"
                }
            ]
        }
    }

class UpdateMovie(BaseModel):
    title: str = Field(default="titulo por defecto")
    overview: str = Field(default="descripcion por defecto")
    year: int = Field(default=2024)
    rating: float = Field(default=0)
    category: str = Field(default="categoria por defecto")

# Listado de películas (Simulación de Base de Datos) Forma 1 de hacerlo
# movies = [
#     {
#         "id": 1,
#         "title": "Avatar",
#         "overview": "En un exuberante planeta llamado Pandora viven los Na'vi...",
#         "year": 2009,
#         "rating": 7.8,
#         "category": "Acción"
#     },
#     {
#         "id": 2,
#         "title": "Avatar 2",
#         "overview": "En un exuberante planeta llamado Pandora viven los Na'vi...",
#         "year": 2022,
#         "rating": 7.8,
#         "category": "Acción"
#     },
#     {
#         "id": 3,
#         "title": "Los locos Adams",
#         "overview": "Risas y más risas",
#         "year": 2019,
#         "rating": 9.0,
#         "category": "Comedia"
#     }
# ]

movies: List[Movie] = [] #aca voy a guardar las peliculas, se pone List y entre corchetes el modelo de la clase

# --- RUTAS DE LA APLICACIÓN ---

@app.get("/", tags=["Home"])
def get_home():
    return HTMLResponse('<h1>Respuesta desde FastAPI</h1>')

# --- SECCIÓN: MOVIES (CRUD) ---

# 1. Crear una nueva película (POST)
#@app.post("/movies", tags=["Movies"])
# Forma 1 de realizarlo
# def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
#     new_movie = {
#         "id": id,
#         "title": title,
#         "overview": overview,
#         "year": year,
#         "rating": rating,
#         "category": category
#     }
#     movies.append(new_movie)
#     return {"message": "Película registrada con éxito", "movie": new_movie}

# Forma 2 de realizarlo(Schemas)
@app.post("/movies", tags=["Movies"])
def create_movie(movie:CreateMovie):# metodo 2 de obtener datos de la peticion create_movie(movie:Movie):
    movies.append(movie)# otra opcion es: movies.append(movie.model_dump())
    return [movie.model_dump() for movie in movies] # otra opcion es: return movies

# 2. Obtener todas las películas (GET)
@app.get("/movies", tags=["Movies"])
def get_movies() -> List[Movie]:#El -> List[Movie] se cambio de tener el ejemplo anterior de Movie a tener List[Movie] porque antes se retornaba un solo objeto y ahora se retorna una lista con muchos objetos
    return movies

# 3. Filtrar películas por categoría y año (GET - Query Parameters)
@app.get("/movies/", tags=["Movies"])
def get_movies_by_category(category: str, year: int):
    results = [movie for movie in movies if movie["category"] == category and movie["year"] == year]
    return results if results else {"message": "No se encontraron coincidencias"}

# 4. Obtener una película por ID (GET - Path Parameters)
@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return {"message": "Película no encontrada"}

# 5. Actualizar una película existente (PUT)
# @app.put("/movies/{id}", tags=["Movies"])Forma 2 de realizarlo solo cambie el def update_movie(id: int, Movie:Movie)(Schemas)
# def update_movie(id: int, Movie:Movie):
#     for item in movies:
#         if item["id"] == id:
#             item["title"] = Movie.title
#             item["overview"] = Movie.overview
#             item["year"] = Movie.year
#             item["rating"] = Movie.rating
#             item["category"] = Movie.category
#             return {
#                 "message": "Película actualizada con éxito", 
#                 "current_movies": movies
#             }
#     return {"message": "Película no encontrada"}

# Forma 2 de realizarlo(Schemas)
@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, Movie:UpdateMovie):
    for item in movies:
        if item["id"] == id:
            item["title"] = Movie.title
            item["overview"] = Movie.overview
            item["year"] = Movie.year
            item["rating"] = Movie.rating
            item["category"] = Movie.category
            return {
                "message": "Película actualizada con éxito", 
                "current_movies": movies
            }
    return {"message": "Película no encontrada"}

# 6. Eliminar una película (DELETE)
@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int): 
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return {
                "message": "Película eliminada con éxito",
                "current_movies": movies
            }
    return {"message": "Película no encontrada"}


# --- OTRAS SECCIONES (Práctica) ---

@app.get("/users", tags=["Users"])
def get_users():
    return {"message": "Lista de usuarios registrados."}

@app.get("/reviews", tags=["Reviews"])
def get_reviews():
    return {"message": "Listado de reseñas de las películas."}