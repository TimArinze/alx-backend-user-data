#!/usr/bin/env python3
"""
a class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication"""
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        if not path.endswith("/"):
            path = path + "/"

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        if request is None:
            return None
        if "Authorization" not in request.headers.keys():
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User"""
        if request is None:
            return None

    def session_cookie(self, request=None):
        """Returns session cookies"""
        if request is None:
            return None
        return request.cookies.get(os.getenv("SESSION_NAME"))
