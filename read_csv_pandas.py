import pandas as pd

time_cols= ['tpep_dropoff_datetime', 'tpep_pickup_datetime']
df = pd.read_csv('C:\\Users\\SiddharthSujir\\Documents\\Training\\Ex_Files_Data_Ingestion_Python\\ExerciseFiles\\Ch02\\02_01\\taxi.csv.bz2', parse_dates=time_cols)

print(df.dtypes)
print(df)
