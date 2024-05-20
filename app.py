from flask import Flask
from flask_migrate import Migrate
from models import db
from urls import configure_routes
from dotenv import load_dotenv
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_fallback_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
load_dotenv()
db.init_app(app)
migrate = Migrate(app, db)

configure_routes(app)

if __name__ == "__main__":
    app.run(port=5001)


