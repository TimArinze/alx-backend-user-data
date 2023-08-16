#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, jsonify, request, abort, url_for, redirect
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
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response, 200
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """Log out"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(int(user.id))
        return redirect("/")
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
