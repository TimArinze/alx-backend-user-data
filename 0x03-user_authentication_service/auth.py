#!/usr/bin/env python3
"""Hash the password"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hash password"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


class Auth:
    """Auth class to interact with the authentication database"""

    def __init__(self):
        """Initializing"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register User"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            return Auth._db.add_user(email, _hash_password(password))
