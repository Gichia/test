import os
import psycopg2


class InitDb(object):
    
    def __init__(self):
        self.app = None
        self.conn = None
        self.curr = None

    def init_db(self, app):
        self.app = app
        self.conn = psycopg2.connect(dbname=os.getenv("DATABASE_NAME"), user=os.getenv("DATABASE_USER"),
                            password=os.getenv("DATABASE_PASS"), host=os.getenv("DATABASE_HOST"))
        self.curr = self.conn.cursor()