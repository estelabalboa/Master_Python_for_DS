"""ETL from CSV to Database: sqlite3"""
import sqlite3
import csv
from datetime import datetime
import logging


def parse_date(text):
    return datetime.strptime(text, '%Y%m%d')


def parse_temperatures(text):
    celsius = float(text) * 10
    return (celsius * 9/5) + 32


converts = [
    ('DATE', 'day', parse_date),
    ('TMIN', 'min_temp', parse_temperatures),
    ('TMAX', 'max_temp', parse_temperatures),
    ('SNOW', 'snow', int)
]


def records_to_db(records):
    object = {}
    for source, destination, conv in converts:
        try:
            object[destination] = conv(records[source])
        except ValueError:
            return None
    return object


def iter_records(csv_file):
    with open(csv_file) as fp:
        for lnum, records in enumerate(csv.DictReader(fp), 2):
            object = records_to_db(records)
            if not object:
                logging.warning('%s:%d Skipping bad record', csv_file, lnum)
                continue
            yield object


sql_schema = '''
    CREATE TABLE IF NOT EXISTS weather (
    day DATE,
    min_temp FLOAT,
    max_temp FLOAT,
    snow INTEGER
    );
    
    CREATE INDEX IF NOT EXISTS weather_day on weather(day);
'''

insert_sql = '''
    INSERT INTO weather (day, min_temp, max_temp, snow)
    VALUES (
    :day, :min_temp, :max_temp, :snow
    );
'''


def etl(csv_file, db_file):
    with sqlite3.connect(db_file) as db:
        cur = db.cursor()
        cur.executescript(sql_schema)
        cur.executemany(insert_sql, iter_records(csv_file))
        return cur.rowcount


if __name__ == '__main__':
    count = etl ('weather.csv', 'db_weather.db')
    print(f'Inserted {count} records')

