from fastapi import FastAPI, Form, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from jose import jwt

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users = {
    "Santiago":{"username":"Santiago Joya","email":"santiagojoyab@outlook.com","password":"Santyjoya02"},
    "user2":{"username":"user2","email":"user2@gmail.com","password":"user2"}
}

def encode_token(payload: dict) -> str:#En este lo que estoy haciendo es coger el payload y convertirlo en un JWT token, esto nos sirve para pasarlo entre aplicaciones
    token = jwt.encode(payload,key="Venkattor2002",algorithm="HS256")
    return token

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:#Es este lo que hace es coger el JWT token y convertirlo en un diccionario, esto nos sirve para pasarlo entre aplicaciones
    data_token = jwt.decode(token,key="Venkattor2002",algorithms=["HS256"])
    user = users.get(data_token["username"])
    return user

#Forma 1 de hacerlo sin el OAuth2PasswordRequestForm
# @app.post("/token")
# def login(username = Form(...), password = Form(...)):
#     return "token"

#Forma 2 de hacerlo con el OAuth2PasswordRequestForm
@app.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(form_data.username)
    if not user or form_data.password != user["password"]:
        raise HTTPException(status_code=401,detail="Usuario no encontrado y/o contraseña incorrecta")
    token = encode_token({"username": form_data.username, "email": user["email"]})#Esto es como generar el JWT token, cuando vamos a implementar JWT hay que cambiar esto
    return {"access_token": token, "token_type": "bearer"}

@app.get("/users/profile")
def profile(my_user:Annotated[dict, Depends(decode_token)]):
    return my_user