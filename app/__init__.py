from flask import Flask
from .DBAccess import DBAccess

app = Flask(__name__)

# Import the route functions from app.py
from . import app