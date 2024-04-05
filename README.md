# Proyecto Flask

Este es un proyecto Flask diseñado para gestionar datos de sensores ambientales. La aplicación proporciona endpoints para cargar datos de sensores y obtener un resumen de los valores promedio.

## Ejecución de la Aplicación

Para ejecutar la aplicación Flask, sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema. Puedes descargar e instalar Python desde [python.org](https://www.python.org/downloads/).

2. Instala las dependencias necesarias ejecutando el siguiente comando en la raíz del proyecto:

   ```bash
   pip install Flask Flask-MySQLdb

#Atención!! Por problemas de instalación no contaba con Docker al momento de realizar el trabajo designado, por lo que a continuación expongo los pasos necesarios para demostrar mis conocimientos en la herramienta

# Dockerfile

   ```bash
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   EXPOSE 5000
   CMD ["python", "app.py"]

# Bash

   docker build -t my-flask-app .
   docker run -d -p 5000:5000 --name my-flask-container my-flask-app
