from app.api.models.basemodel import BaseModel
from app.api import ver2

db = BaseModel()

@ver2.route("/", methods=["GET"])
def home():
    """Register new user endpoint"""

    users = db.get_all()

    return users