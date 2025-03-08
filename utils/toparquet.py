import pandas as pd

def leer_parquet(file):
    df = pd.read_parquet(file, engine='fastparquet')
    return df

def escribir_parquet(df, file):
    df.to_parquet(file, engine='fastparquet')