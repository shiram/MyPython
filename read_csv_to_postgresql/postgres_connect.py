import psycopg2
from config import config

def connect():
    # Attempt to connect to postgresql database server
    conn = None
    params = config()
    print('Connection to Database Started***')
    conn = psycopg2.connect(**params)

    return conn
