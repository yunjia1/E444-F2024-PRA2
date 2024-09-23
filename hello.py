from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', name = 'World',
                           current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('index.html', name=name, current_time=datetime.utcnow())