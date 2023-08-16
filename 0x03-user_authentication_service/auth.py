#!/usr/bin/env python3
"""Hash the password"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hash password"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """Generates UUID"""
    return str(uuid.uuid4())


"""Register user"""


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
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Credentials validation"""
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session and get session ID"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            new_session_id = setattr(user, "session_id", session_id)
            self._db._session.commit()
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """FInd user by session_id"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user,
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int):
        """Destroy session"""
        try:
            self._db.update_user(user_id, session_id=None)
            return None
        except ValueError:
            return None
