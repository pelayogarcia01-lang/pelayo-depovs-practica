# a. Utiliza la imagen base de Python
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# b & c. Copia e instala dependencias para aprovechar el cache
# Asegúrate de que requirements.txt exista y esté completo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# d. Copia el código fuente de la aplicación
# (Ajusta la ruta si tu código no está en ./src)
COPY src/ src/

# f. Comando de inicio (ejecuta el script principal)
# Reemplaza 'main.py' con tu script ejecutable si tiene otro nombre
CMD ["python", "src/main.py"]
