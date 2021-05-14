import bz2
import csv
from collections import namedtuple
from datetime import datetime

Column = namedtuple('Column', 'src dest convert')


def parse_timestamp(text):
    return datetime.strptime(text, '%Y-%m-%d %H:%M:%S')


columns = [
    Column('VendorID', 'vendor_id', int),
    Column('passenger_count', 'num_passengers', int),
    Column('tip_amount', 'tip', float),
    Column('total_amount', 'price', float),
    Column('tpep_dropoff_datetime', 'dropoff_time', parse_timestamp),
    Column('tpep_pickup_datetime', 'pickup_time', parse_timestamp),
    Column('trip_distance', 'distance', float)
]


def iterate_file(file_name):
    with bz2.open(file_name, 'rt') as fp:
        reader = csv.DictReader(fp)
        for csv_record in reader:
            record = {}
            for col in columns:
                value = csv_record[col.src]
                record[col.dest] = col.convert(value)
            yield record

def example():
    from pprint import pprint
    file_name = 'C:\\Users\\SiddharthSujir\\Documents\\Training\\Ex_Files_Data_Ingestion_Python\\ExerciseFiles\\Ch02\\02_01\\taxi.csv.bz2'
    for i, record in enumerate(iterate_file(file_name)):
        if i >= 10:
            break
        print(record)

example()
