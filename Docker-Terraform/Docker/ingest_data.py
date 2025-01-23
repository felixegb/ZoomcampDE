import os
import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine



def main (params):
    
    user = params.user
    passw = params. passw
    host = params.host
    port = params. port
    db = params.db
    table_name = params.table_name
    url = params.url
    
    csv_name = 'F:/data_engineer/archivo.csv'
    os.system(f'wget {url} -O {csv_name}')
    
    engine = create_engine(f'postgresql://{user}:{passw}@{host}:{port}/{db}')


    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)


    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    df.to_sql(name='nueva_tabla', con=engine, if_exists='append')

    while True:
        t_start =  time()
        
        df = next(df_iter)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
        df.to_sql(name=table_name, con=engine, if_exists='append')
        
        t_end = time()
        
        print ('insert took %.3f secound' %(t_end - t_start))
    
    


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='ingest csz to postgres')

    parser.add_argument('--user', help = 'user name for postgres')
    parser.add_argument('--passw', help = 'pass for postgres')
    parser.add_argument('--host', help = 'host for postgres')
    parser.add_argument('--port', help = 'port for postgres')
    parser.add_argument('--db', help = 'db name for postgres')
    parser.add_argument('--table_name', help = 'name of the table')
    parser.add_argument('--url', help = 'url of the csv')

    args = parser.parse_args()
    #print (args.accumulate(args.integers))
    main(args)


""" para linux   python ingest_data.py \
    --user=root \
    --passw=root\
    --host=localhost \
    --port=5432 \ 
    --db=ny_taxi \
    --table_name=tabla_txi \
    --url='archivo.cvs' 
    
    para win python ingest_data.py `
    --user=root `
    --passw=root `
    --host=localhost `
    --port=5432 `
    --db=ny_taxi `
    --table_name=tabla_txi `
    --url="archivo.cvs"
    
    """