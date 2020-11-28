from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)


from app import routes

