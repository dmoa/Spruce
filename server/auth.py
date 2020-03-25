from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app import db
from server.models import User, user_schema

auth_blueprint = Blueprint("api", __name__, url_prefix="/auth")


@auth_blueprint.route("/login", methods=("GET", "POST"))
def login():
    identifier = request.json["identifier"]
    if not identifier:
        identifier = request.json["username"]
        if not identifier:
            identifier = request.json["email"]
    password = request.json["password"]

    user = User.query.filter((User.username == identifier) | (User.email == identifier)).first()
    if not user:
        return jsonify({
            "type": "error",
            "message": "That user doesn't exist.",
            "suggestion": "Try registering first."
        })

    if user.check_password(password):
        return jsonify({
            "type": "success+data",
            "data": create_access_token(user_schema.dump(user))
        })


@auth_blueprint.route("/register")
def register():
    username = request.json["username"]
    email = request.json["email"]
    password = request.json["password"]
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        "type": "success",
        "message": "Created that user.",
        "suggestion": ""
    })
