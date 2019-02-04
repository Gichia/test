''' Creates the base of the API'''
from instance.config import app_config
from app import create_app

app = create_app(config_name="development")

if __name__ == "__main__":
    app.run()