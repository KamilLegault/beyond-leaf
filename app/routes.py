from flask import render_template, flash, redirect, request, make_response, jsonify
from app import app
from werkzeug.utils import secure_filename
import os


@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index-simple-ed.html')
