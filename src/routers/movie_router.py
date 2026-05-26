from typing import List
from fastapi import Path, Query, Body, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import (
    JSONResponse,
    HTMLResponse,
    PlainTextResponse,
    RedirectResponse,
    FileResponse,
)
from src.models.movie_model import Movie, CreateMovie, UpdateMovie

movies: List[Movie] = []  # aca voy a guardar las peliculas, se pone List y entre corchetes el modelo de la clase
movie_router = APIRouter()  # Contiene las rutas que tienen que ver con pelicuas

# --- SECCIÓN: MOVIES (CRUD) ---

# 1. Crear una nueva película (POST)
# @app.post("/movies", tags=["Movies"])
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
@movie_router.post("/", tags=["Movies"])
def create_movie(
    movie: CreateMovie,
):  # metodo 2 de obtener datos de la peticion create_movie(movie:Movie):
    movies.append(movie.model_dump())  # otra opcion es: movies.append(movie.model_dump())
    return movies

    # Esta es otra rta de JSONResponse
    # content = [movie.model_dump() for movie in movies] # otra opcion es: return movies
    # return JSONResponse(content=content)

    # Otra rta es
    # return RedirectResponse("/movies", status_code=200)


# 2. Obtener todas las películas (GET)
@movie_router.get("/by_category",tags=["Movies"],status_code=201,response_description="Respuesta exitosa",)
def get_movies() -> List[Movie]:
    return JSONResponse(content=jsonable_encoder(movies), status_code=400)


# 3. Filtrar películas por categoría y año (GET - Query Parameters)
@movie_router.get("/", tags=["Movies"])
def get_movies_by_category(category: str = Query(default=None, min_length=5, max_length=50),):
    results = [movie for movie in movies if movie["category"] == category]
    return results if results else {"message": "No se encontraron coincidencias"}


# 4. Obtener una película por ID (GET - Path Parameters)
@movie_router.get("/{id}", tags=["Movies"])
def get_movie(id: int = Path(ge=1, le=2000)):
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
@movie_router.put("/{id}", tags=["Movies"])
def update_movie(id: int, Movie: UpdateMovie):
    for item in movies:
        if item["id"] == id:
            item["title"] = Movie.title
            item["overview"] = Movie.overview
            item["year"] = Movie.year
            item["rating"] = Movie.rating
            item["category"] = Movie.category
            return {
                "message": "Película actualizada con éxito",
                "current_movies": movies,
            }
    return {"message": "Película no encontrada"}


# 6. Eliminar una película (DELETE)
@movie_router.delete("/{id}", tags=["Movies"])
def delete_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)
            return {"message": "Película eliminada con éxito", "current_movies": movies}
    return {"message": "Película no encontrada"}
