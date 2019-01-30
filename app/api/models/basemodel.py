from app import database

class BaseModel(object):

    def get_all(self):
        database.curr.execute("SELECT * FROM app_users")
        items = database.curr.fetchall()
        return items