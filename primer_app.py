from fastapi import FastAPI

# Esto es una instancia de FastAPI
app = FastAPI() # Esta linea crea la instancia de la clase FastAPI.

# Esto es un decorador, se usa para indicar que la siguiente funcion es un manejador de peticiones.
@app.get("/") 
# Esta funcion se ejecuta cuando se recibe una peticion GET a la raiz de la aplicacion.
def home():
    # Esto es un diccionario, se usa para enviar datos a la aplicacion.
    return {"Hello": "World"}