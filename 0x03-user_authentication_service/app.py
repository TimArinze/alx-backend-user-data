#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", strict_slashes=False)
def basic():
    """Basic flask app"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """Register User"""
    data = request.form
    email = data["email"]
    password = data["password"]
    if email:
        try:
            AUTH.register_user(email, password)
            return jsonify({"email": email, "message": "user created"}), 200
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """Log in"""
    data = request.form
    email = data["email"]
    password = data["password"]
    if AUTH.valid_login(email, password):
        AUTH.create_session(email)
        return jsonify({"email": email, "message": "logged in"}), 200
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
