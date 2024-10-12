from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os  # Import the os module for generating a random key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set a secret key for the session management
app.secret_key = os.urandom(24)  # Generates a random key

db = SQLAlchemy(app)

from app import routes, models
