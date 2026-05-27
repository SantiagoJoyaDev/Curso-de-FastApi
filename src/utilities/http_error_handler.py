from fastapi import FastAPI, status
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse

class HTTPErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:#Aqui en app se coloca FastAPI() porque es la instancia de la aplicación
        super().__init__(app)#El super es para que la función sea llamada por defecto, osea que se ejecute la función constructora de la clase padre, en este caso, la clase BaseHTTPMiddleware
    
    async def dispatch(self, request: Request, call_next) -> Response:# El async es para que la función sea asíncrona y pueda manejar peticiones concurrentes,
        #el dispatch es para que la función sea llamada cada vez que se hace una petición
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"ERROR -- Contenido no disponible": str(e)},#Esto es para capturar cualquier error que ocurra en la aplicación
            )
# Esto es un Middleware usando Starlette, ya que FastAPI se basa en Starlette para su funcionamiento interno.
# Esto quiere decir que si ocurre un error en la aplicación, se ejecutará el dispatch y se devolverá la respuesta con el mensaje de error.