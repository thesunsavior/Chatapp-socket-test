from flask import render_template
from chat_app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")