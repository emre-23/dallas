from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to my app'

@app.route('/status')
def index():
    return 'index'
