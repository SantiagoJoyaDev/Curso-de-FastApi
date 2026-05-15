# FastApi  Es un microframework moderno,rapido (alto rendimiento) para la construccion de APIs web con Python 3.10+ basado en las 
# anotaciones de tipos (type hints) y standard (PEP 484) de Python.

# Características principales:
# 1. Alto rendimiento: Es uno de los frameworks más rápidos de Python.
# 2. Facilidad de uso: Su sintaxis es sencilla e intuitiva.
# 3. Validación de datos: Usa Pydantic para la validación de datos.
# 4. Documentación automática: Genera documentación automática de la API (Swagger UI y ReDoc).
# 5. Concurrencia: Soporta programación asíncrona con `async` y `await`.
# 6. Validación de datos: Usa Pydantic para la validación de datos.
# 7. Autocompletado: Gracias a las anotaciones de tipos, ofrece autocompletado en los IDEs.

# Marco mas utilizado por FastAPI para la validación de datos:
# Starlette --> Para la ejecucion del servidor
# Pydantic --> Para la validación de datos
# Uvicorn --> Para la ejecucion del servidor

# Parametros de ruta: Son variables que se pueden pasar a las rutas de una API. Se utilizan para indicar que una parte de la ruta es una variable. Por ejemplo, en la ruta /movies/{id}, 
# el parametro {id} es una variable que se puede pasar a la ruta para indicar que queremos obtener una pelicula con un id especifico.