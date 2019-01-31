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

    data = request.get_json()

    db.post_meetup(data["user"], data["location"], data["topic"], data["happeningOn"], data["tags"])
    return jsonify({"status": "OK"})