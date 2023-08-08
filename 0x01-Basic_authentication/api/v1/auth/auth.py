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

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User"""
        if request is None:
            return None 
