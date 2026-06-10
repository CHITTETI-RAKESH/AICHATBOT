from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from flask_bcrypt import Bcrypt

from database.models import (
    db,
    User
)

auth = Blueprint(
    "auth",
    __name__
)

bcrypt = Bcrypt()


@auth.route("/register",
            methods=["GET", "POST"])

def register():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        hashed = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        user = User(
            username=username,
            email=email,
            password=hashed
        )

        db.session.add(user)
        db.session.commit()

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "register.html"
    )


@auth.route("/login",
            methods=["GET", "POST"])

def login():

    return render_template(
        "login.html"
    )
