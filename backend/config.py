from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialise Flask app and enable cross origin requests
app = Flask(__name__)
CORS(app)

# Define sqlite local database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

# False: doesn't track mods made to the database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Creates a db instance for app with access to the configs mentioned above
db = SQLAlchemy(app)