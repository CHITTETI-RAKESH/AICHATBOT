from flask import Blueprint
from flask import request
from flask import jsonify

from flask_login import (
current_user,
login_required
)

from database.models import (
db,
ChatHistory
)

from services.ai_service import (
ask_ai
)

from services.memory_service import (
build_context
)

chat = Blueprint(
"chat",
__name__
)


@chat.route("/chat")

@login_required

def chat_page():

    from flask import render_template

    return render_template(
        "chat.html"
    )


@chat.route("/ask",
methods=["POST"])

@login_required

def ask():

    data = request.json

    message = data["message"]

    history = ChatHistory.query.filter_by(
        user_id=current_user.id
    ).all()

    context = build_context(
        history,
        message
    )

    response = ask_ai(
        context
    )

    chat_record = ChatHistory(

        user_id=current_user.id,

        question=message,

        answer=response
    )

    db.session.add(
        chat_record
    )

    db.session.commit()

    return jsonify(
        {
            "response":
            response
        }
    )
