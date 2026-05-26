import datetime
from pydantic import BaseModel, Field, validator

# MODELOS o SCHEMAS
# Definición del Modelo de Datos (Esquema de la Película) Forma 2 de realizarlo(Schemas)
class Movie(BaseModel):
    # id: Optional[int] = None Forma 2 de realizarlo
    # Otra manera de hacerlo es poner : int | None = None
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str


class CreateMovie(BaseModel):  # Validaciones con Field
    id: int
    title: str = Field(min_length=5, max_length=15, default="titulo por defecto")
    overview: str = Field(min_length=5, max_length=500, default="descripcion por defecto")
    year: int = Field(le=datetime.datetime.now().year, default=2024)  # otra manera de hacerlo Field(ge=1800, le=2023)
    rating: float = Field(ge=0, le=10, default=0)
    category: str = Field(min_length=5, max_length=50, default="categoria por defecto")
    # gt es mayor que, lt es menor que, ge es mayor o igual que, le es menor o igual que
    # ge 1800 y le 2023, significa que el año debe ser mayor o igual a 1800 y menor o igual a 2023
    # lt 0 y ge 10, significa que la calificacion debe ser menor que 0 y mayor o igual a 10
    # le 50, significa que la categoria debe ser menor o igual a 50
    # le datetime.datetime.now().year, significa que el año debe ser menor o igual al año actual

    model_config = {  # Esto es para la documentacion de swagger y obtener ejemplos osea para que se muestre el ejemplo al momento de crear la pelicula
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Avatar",
                    "overview": "En un exuberante planeta llamado Pandora viven los Na'vi...",
                    "year": 2009,
                    "rating": 7.8,
                    "category": "Accion",
                }
            ]
        }
    }

    # Otra manera de hacerlo con @validator y de forma dinamica: (Valiacion personalizada)
    @validator("rating")
    def validate_rating(cls, value):
        if value < 0 or value > 10:
            raise ValueError("La calificación debe estar entre 0 y 10")# raise es para lanzar un error
        return value


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