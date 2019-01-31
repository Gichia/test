import os
from flask import request, jsonify
from app.api.models.basemodel import BaseModel
from app.api import ver2

db = BaseModel()

@ver2.route("/", methods=["GET"])
def home():
    """Register new user endpoint"""

    users = db.get_all()

    return jsonify({"data": users, "db": os.getenv("TEST_DATABASE_URL"), "status": 200})


@ver2.route("/", methods=["POST"])
def post_home():
    """Register new user endpoint"""

    try:
        data = request.get_json()
        user = data["user"]
        location = data["location"]
        topic = data["topic"]
        happeningon = data["happeningOn"]
        tags = data["tags"]
        db.post_meetup(user, location, topic, happeningon, tags)
    except:
        return jsonify({"status": 500, "message": "Provide all details"})

    return jsonify({"status": "OK"})


@ver2.route("/get/<int:meetup_id>", methods=["POST"])
def get_specific(meetup_id):
    """Register new user endpoint"""

    data = db.get_meetup_id(meetup_id)

    if not data:
        return jsonify({"status": 404})

    return jsonify({"id": data, "status": 200})