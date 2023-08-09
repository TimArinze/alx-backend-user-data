#!/usr/bin/env python3
"""
Basic Auth
"""
from api.v1.auth.auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """Base64 decode"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode("utf-8")
            return decoded_string
        except binascii.Error:
            return None