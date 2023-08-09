#!/usr/bin/env python3
"""
Basic Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Base64 part"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header.startswith("Basic ") is False:
            return None
        else:
            return authorization_header.split(" ")[-1]
