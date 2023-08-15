#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")