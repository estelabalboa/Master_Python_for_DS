"""Load & converting data from CSV using Pandas"""
import pandas as pd

time_cols = ['tpep_dropoff_datetime', 'tpep_pickup_datetime']


def load_df(file_name):
    return pd.read_csv('Ex_Files_Data_Ingestion_Python/Exercise Files/Ch02/02_01/taxi.csv.bz2', parse_dates=time_cols)


print(load_df('Ex_Files_Data_Ingestion_Python/Exercise Files/Ch02/02_01/taxi.csv.bz2').head())


def iter_df(file_name):
    yield from pd.read_csv(
        'Ex_Files_Data_Ingestion_Python/Exercise Files/Ch02/02_01/taxi.csv.bz2', parse_dates=time_cols, chunksize=100)


for i, df in enumerate(iter_df('Ex_Files_Data_Ingestion_Python/Exercise Files/Ch02/02_01/taxi.csv.bz2')):
    if i > 10:
        break
    print(len(df))
