from flask import Flask
from app.model import Model

app = Flask(__name__)
model = Model()

from app import views
