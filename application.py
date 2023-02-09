# wsgi.py
import random
from flask import Flask, jsonify
application = Flask(__name__)
@application.route('/')
def home():
    return jsonify({ 'roll': random.randint(1,6) })
