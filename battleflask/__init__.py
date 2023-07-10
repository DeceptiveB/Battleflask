from flask import Flask, render_template, url_for
from battleflask.auth import bp

app = Flask(__name__)

app.register_blueprint(auth.bp, url_prefix="/")
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
users = list()

from battleflask import routes
