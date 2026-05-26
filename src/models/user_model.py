
import datetime
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=50)
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=5, max_length=50)
    age: int = Field(le=datetime.datetime.now().year)
    gender: str
    role: str

class CreateUser(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=50)
    email: str = Field(min_length=15, max_length=50)
    password: str = Field(min_length=8, max_length=50)
    age: int = Field(le=datetime.datetime.now().year)
    gender: str
    role: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "name": "Juan",
                    "email": "[EMAIL_ADDRESS]",
                    "password": "[PASSWORD]",
                    "age": 25,
                    "gender": "Masculino",
                    "role": "Usuario",
                }
            ]
        }
    }

class UpdateUser(BaseModel):
    id: int = Field(default=0)
    name: str = Field(default="nombre por defecto")
    email: str = Field(default="[EMAIL_ADDRESS]")
    password: str = Field(default="[PASSWORD]")
    age: int = Field(default=18)
    gender: str = Field(default="Masculino")
    role: str = Field(default="Usuario")