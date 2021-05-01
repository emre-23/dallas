from flask import Flask, url_for
from flask import render_template
from markupsafe import escape
from flask import abort, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to my app'

@app.route('/status')
def index():
    return '', 204
