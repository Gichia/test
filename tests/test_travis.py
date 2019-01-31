"""File to test all meetup endpoints"""
import os
import psycopg2 as pg2
import json
from tests.basetest import BaseTest

data = {
	"topic": "The Test Topic",
	"location": "Another Test Location",
	"happeningOn": "12/12/2019",
	"tags": ["WebDev", "Flask"],
	"user": 1
}

class TestMeetups(BaseTest):
    """ Class to test all user endpoints """

    def test_get_meetups(self):
        """Method to test get all meetups endpoint"""
        url = "http://localhost:5000/api/v2/"

        response = self.get_items(url)
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 200)

    def test_post_meetup(self):
        """Method to test post meetup endpoint"""
        url = "http://localhost:5000/api/v2/"

        response = self.post(url, data)
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], "OK")

    def test_get_specific_meetup(self):
        """Method to test inaccurate data"""
        id = self.get_meetup_id()
        url = "http://localhost:5000/api/v2/get/{}".format(id)

        response = self.post(url, data)
        result = json.loads(response.data.decode("UTF-8"))

        self.assertEqual(result["status"], 200)