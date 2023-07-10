from battleflask import app
from battleflask.auth import users
from flask import render_template, jsonify, session, Response
from .models import User, Message
from .utils import get_user_by_username

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def get_online_users():
    usernames = list(map(lambda x: x.name, users))
    response = jsonify(users= usernames)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/messages")
def get_messages():
    for u in users:
        if True: #u == session["username"]:
            response = jsonify(messages = u.messages)
            print(u.messages)
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response

@app.route("/new_game")
def new_game():
    return render_template("game.html")

@app.route("/<username>/invite")
def invite(username):
    for u in users:
        if u.username == username:
           u.new_message(session["username"])
