"""Base Class for our tests"""
import os
import unittest
import json
import psycopg2 as pg2
import jwt
import datetime
from instance.config import Config
from app import create_app

data = {
	"topic": "The Test Topic",
	"location": "Another Test Location",
	"happeningOn": "12/12/2019",
	"tags": ["WebDev", "Flask"],
	"user": 1
}

class BaseTest(unittest.TestCase):
    """Initializes our setUp for tests"""
    def setUp(self):
        """Initializes our app and tests"""
        db_url = os.getenv("DATABASE_URL")
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.db = pg2.connect(db_url)
        self.curr = self.db.cursor()

        self.client.post("http://localhost:5000/api/v2/", data=json.dumps(data), content_type="application/json")

    def post(self, url, data):
        """Method for post tests"""
        return self.client.post(url, data=json.dumps(data), content_type="application/json")

    def get_items(self, url):
        """Method for get tests"""
        return self.client.get(url)

    def tearDown(self):
        """Tear down the app after running tests"""
        query = """DELETE FROM meetups WHERE topic='The Test Topic'"""
        self.curr.execute(query)
        self.db.commit()
        self.curr.close()
        self.db.close()