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
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Credentials validation"""
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                return False
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session and get session ID"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            setattr(user, "session_id", session_id)
            self._db._session.commit()
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """FInd user by session_id"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int):
        """Destroy session"""
        try:
            self._db.update_user(user_id, session_id=None)
            return None
        except ValueError:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Generate reset password token"""
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return user.reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str):
        """Update password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_password,
                                 reset_token=None)
        except NoResultFound:
            raise ValueError
