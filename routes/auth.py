from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

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
methods=["GET","POST"])

def register():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        existing = User.query.filter_by(
            email=email
        ).first()

        if existing:

            flash("Email already exists")

            return redirect(
                url_for("auth.register")
            )

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

        flash("Registration Successful")

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "register.html"
    )


@auth.route("/login",
methods=["GET","POST"])

def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            password
        ):

            login_user(user)

            return redirect(
                url_for("auth.dashboard")
            )

        flash("Invalid Credentials")

    return render_template(
        "login.html"
    )


@auth.route("/dashboard")

@login_required

def dashboard():

    return render_template(
        "dashboard.html"
    )


@auth.route("/logout")

@login_required

def logout():

    logout_user()

    return redirect(
        url_for("auth.login")
    )
