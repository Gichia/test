''' Creates the base of the API'''
from instance.config import app_config
from app import create_app

# env = app_config['development']
app = create_app("development")

if __name__ == "__main__":
    app.run()
