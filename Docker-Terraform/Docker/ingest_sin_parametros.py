import os
import pandas as pd
from sqlalchemy import create_engine
from time import time


def main():
    
    # Parámetros definidos directamente en el script
    user = 'root'
    passw = 'root'
    host = 'localhost'
    port = '5432'
    db = 'ny_taxi'
    table_name = 'tabla_taxi'
    url = 'F:/data_engineer/archivo.csv'
    
    #csv_name = 'F:/data_engineer/archivo.csv'
    csv_name = '/app/data/archivo.csv' #para usar volumen
    
    if not os.path.exists(csv_name):
    # Solo descarga si el archivo no existe
        os.system(f'wget {url} -O {csv_name}')
    else:
        print(f"El archivo {csv_name} ya existe. No se descargará.")

    #os.system(f'wget {url} -O {csv_name}')
    
    engine = create_engine(f'postgresql://{user}:{passw}@{host}:{port}/{db}')

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    df.to_sql(name='nueva_tabla', con=engine, if_exists='append')

    while True:
        t_start = time()
        
        df = next(df_iter)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
        df.to_sql(name=table_name, con=engine, if_exists='append')
        
        t_end = time()
        
        print('insert took %.3f second' % (t_end - t_start))


if __name__ == '__main__':
    main()
