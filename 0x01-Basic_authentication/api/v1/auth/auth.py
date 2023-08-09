#!/usr/bin/env python3
"""
a class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication"""
        if path:
            return False

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        if request:
            return None
        if request.headers.get('Authorization'):
            return request.headers.get('Authorization')
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User"""
        if request is None:
            return None

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Defines which routes don't need authentication"""
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
