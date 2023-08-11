#!/usr/bin/env python3
"""
New view for Session Authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """view that handles all flask route"""
    email = request.form.get("email")
    password = request.form.get("password")
    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400
    if password is None or len(password) == 0:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if users is None or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password) is False:
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth
        auth.create_session(user.get("id"))
        return jsonify(user.to_json()), 200
