from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import (JSONResponse)
from src.models.user_model import User, CreateUser, UpdateUser

users: List[User] = []
user_router = APIRouter()

@user_router.post("/users", tags=["Users"])
def create_user(user: CreateUser):
    users.append(user.model_dump())
    return users

@user_router.get("/by_category", tags=["Users"])
def get_users() -> List[User]:
    return JSONResponse(content=jsonable_encoder(users), status_code=400)

@user_router.put("/users/{id}", tags=["Users"])
def update_user(id: int, user: UpdateUser):
    for item in users:
        if item["id"] == id:
            item["name"] = user.name
            item["email"] = user.email
            item["password"] = user.password
            item["age"] = user.age
            item["gender"] = user.gender
            item["role"] = user.role
            return {
                "message": "Usuario actualizado con éxito",
                "current_users": users,
            }
    return {"message": "Usuario no encontrado"}

@user_router.delete("/{id}", tags=["Users"])
def delete_user(id: int):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return {"message": "Usuario eliminado con éxito", "current_users": users}
    return {"message": "Usuario no encontrado"}
