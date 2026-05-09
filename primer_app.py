from fastapi import FastAPI, Body
# El body es para recibir datos de la peticion, y el path es para recibir datos de la ruta
from fastapi.responses import HTMLResponse

# Configuración de la aplicación
app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "1.0.0"

# Listado de películas (Simulación de Base de Datos)
movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi...",
        "year": 2009,
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar 2",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi...",
        "year": 2022,
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 3,
        "title": "Los locos Adams",
        "overview": "Risas y más risas",
        "year": 2019,
        "rating": 9.0,
        "category": "Comedia"
    }
]

# --- RUTAS DE LA APLICACIÓN ---

@app.get("/", tags=["Home"])
def get_home():
    return HTMLResponse('<h1>Respuesta desde FastAPI</h1>')

# --- SECCIÓN: MOVIES (CRUD) ---

# 1. Crear una nueva película (POST)
@app.post("/movies", tags=["Movies"])
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    new_movie = {
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    }
    movies.append(new_movie)
    return {"message": "Película registrada con éxito", "movie": new_movie}

# 2. Obtener todas las películas (GET)
@app.get("/movies", tags=["Movies"])
def get_movies():
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
@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for movie in movies:
        if movie["id"] == id:
            movie["title"] = title
            movie["overview"] = overview
            movie["year"] = year
            movie["rating"] = rating
            movie["category"] = category
            return {
                "message": "Película actualizada con éxito", 
                "movie_updated": movie,
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