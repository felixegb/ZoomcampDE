FROM python:3.12.7

# Instalar wget y las dependencias necesarias
RUN apt-get update && apt-get install -y wget

# Instalar paquetes de Python necesarios
RUN pip install pandas sqlalchemy psycopg2

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo Python al contenedor
COPY ingest_sin_parametros.py ingest_sin_parametros.py

# Establecer el punto de entrada para ejecutar el script Python
ENTRYPOINT ["python", "ingest_sin_parametros.py"]





# para correr el contenedor   docker run -it test:pandas
# para contruir docker build -t nombre:tag .(el pto es pq el dockerfile esta en la misma ubucacion del)