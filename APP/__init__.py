from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

# initialising Flask app
app = Flask(__name__)

# flask app configurations from the config class
app.config.from_object(Config)

# connecting db with flask app
db = SQLAlchemy(app)

from APP import views
