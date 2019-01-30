from app import db



class BaseModel(object):

    def get_all(self):
        db.curr.execute("SELECT * FROM app_users")
        items = db.curr.fetchall()
        return items