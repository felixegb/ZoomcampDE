FROM python:3.12.7

RUN apt-get update && apt-get install -y wget

RUN pip install pandas sqlalchemy psycopg2

# directorio de trabajo dentro del contenedor
WORKDIR /app

COPY ingest_data.py ingest_data.py

ENTRYPOINT ["python", "ingest_data.py"]





# para correr el contenedor   docker run -it test:pandas
# para contruir docker build -t nombre:tag .(el pto es pq el dockerfile esta en la misma ubucacion del)