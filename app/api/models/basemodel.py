import datetime
from app.db_conn import init_connection

db = init_connection()

class BaseModel(object):

    """Base model to initiate db"""
    def __init__(self):
        self.db = init_connection()
        self.curr = init_connection().cursor()

    def get_all(self):
        query = """SELECT email FROM app_users"""

        cursor = self.db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def post_data(self, query, data):
        """Method to post data to db"""
        curr = self.db.cursor()
        res = curr.execute(query, data)
        self.db.commit()
        return res

    def post_meetup(self, user_id, location, topic, happeningon, tags):
        """Method to post a new meetup"""
        meetup = {
            "created_by": user_id,
            "location": location,
            "topic": topic,
            "tags": tags,
            "createdon": datetime.datetime.now(),
            "happeningon": happeningon
        }

        query = """INSERT INTO meetups (created_by, location, topic, tags, createdon, happeningon) 
                VALUES ( %(created_by)s, %(location)s, %(topic)s, %(tags)s, %(createdon)s, %(happeningon)s ) RETURNING meetup_id"""

        data = self.post_data(query, meetup)
        return data

    def get_meetup_id(self, meetup_id):
        # query = """SELECT * FROM meetups WHERE meetup_id=%s"""
        # self.curr.execute(query, (meetup_id,))
        # res = self.curr.fetchone()
        # return res

        query = """SELECT meetup_id FROM meetups WHERE topic='Test Topic Master' LIMIT 1"""
        self.curr.execute(query)
        res = self.curr.fetchone()
        return res