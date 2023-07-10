from flask import Blueprint, render_template, url_for, redirect, request, session
from .models import User
bp = Blueprint("auth", __name__, url_prefix="/auth")

users = list()


@bp.route("/login", methods=("GET", "POST"))
def login():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        username = request.form.get("username")
        if (len(username) < 5):
            error = "Username must be at least 5 characteres."
            return render_template("auth/login.html",error=error)
        elif(username in users):
            error = "Username already taken."
            return render_template("auth/login.html",error=error)
        else:
            session["username"] = username
            user = User(username)
            users.append(user)
            return redirect(url_for("index"))

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


