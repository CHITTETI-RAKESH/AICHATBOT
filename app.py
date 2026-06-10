from flask import Flask
from flask_login import LoginManager

from config import Config

from database.models import (
    db,
    User
)

from routes.auth import auth
from routes.chat import chat

app = Flask(__name__)

app.config.from_object(
    Config
)

db.init_app(app)

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):

    return User.query.get(
        int(user_id)
    )

app.register_blueprint(
    auth
)

app.register_blueprint(
    chat
)

with app.app_context():

    db.create_all()

if __name__ == "__main__":

    app.run(
        debug=True
    )
