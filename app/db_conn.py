import os
import psycopg2 as pg2

db_url = os.getenv('DATABASE_URL')

def init_connection():
    """Function to connect to db through psycopg"""
    conn = pg2.connect(db_url)
    return conn
