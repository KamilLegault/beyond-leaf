from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
import pandas as pd
import os

app = Flask(__name__)
df = pd.read_csv('app/static/results.csv').fillna(0)
app.config.from_object(Config)
bootstrap = Bootstrap(app)


from app import routes

