#!/usr/bin/env python3
"""End-to-end integration test"""
import requests
import json

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Register user"""
    payload = {"email": email, "password": password}
    response = requests.post("{}/users".format(BASE_URL), data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Log in with wrong password"""
    payload = {"email": email, "password": password}
    response = requests.post("{}/sessions".format(BASE_URL), data=payload)
    assert response.status_code == 401


def log_in(email: str, password: str) -> None:
    """Log in with wrong password"""
    payload = {"email": email, "password": password}
    response = requests.post("{}/sessions".format(BASE_URL), data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}


def profile_unlogged() -> None:
    """Profile of unlogged user"""
    response = requests.get("{}/profile".format(BASE_URL))
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """Profile of logged in user"""
    response = requests.get("{}/profile".format(BASE_URL))
    assert response.status_code == 200
    assert response.json() == {"email": EMAIL, "message": "logged in"}


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
