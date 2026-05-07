# Comandos básicos para ejecutar la aplicación:
# 1. Activar el entorno virtual:
#    .\venv\Scripts\activate
# 2. Ejecutar la aplicación:
#    uvicorn main:app --reload
# 3. Abrir el navegador y acceder a:
#    http://localhost:8000
# 4. Acceder a la documentación automática:
#    http://localhost:8000/docs
# 5. Acceder a la documentación interactiva:
#    http://localhost:8000/redoc
# 6. Desactivar el entorno virtual:
#    .\venv\Scripts\deactivate
# 7. Instalar dependencias de un archivo requirements.txt:
#    pip install -r requirements.txt
# 8. para cambiar de puerto
#    uvicorn main:app --reload --port 8080
# 9. Para salir de la aplicacion
#    Ctrl + C
# para conectarlo a otro equipo
#    uvicorn main:app --reload --host [IP_ADDRESS] 
#    con esto se conecta a otros equipos de la red