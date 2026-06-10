from flask import Blueprint
from flask import request
from flask import jsonify

from services.ai_service import (
    generate_response
)

chat = Blueprint(
    "chat",
    __name__
)

@chat.route(
    "/ask",
    methods=["POST"]
)

def ask():

    data = request.json

    question = data["message"]

    answer = generate_response(
        question
    )

    return jsonify(
        {
            "response": answer
        }
    )
