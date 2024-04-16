#!/usr/bin/env python3
""" Module of the Basic Auth Class
"""

import base64
from models.user import User
from api.v1.auth.auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """ Class Basic Auth
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """extract_base64_authorization_header"""
        if (authorization_header is None or
                not isinstance(authorization_header, str)):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header"""
        if (base64_authorization_header is None or
                not isinstance(base64_authorization_header, str)):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Method for extract_user_credentials"""
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str)):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_email, user_password = decoded_base64_authorization_header.split(
                ':', 1)
        return user_email, user_password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Method for user_object_from_credentials"""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({"email": user_email})

        if not users:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Method for current_user"""
        if request is None:
            return None

        authorization_header = self.authorization_header(request)
        if authorization_header is None:
            return None

        base64_authorization_header = self.extract_base64_authorization_header(
                authorization_header)
        if base64_authorization_header is None:
            return None

        decoded_authorization_header = self.decode_base64_authorization_header(
                base64_authorization_header)
        if decoded_authorization_header is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(
                decoded_authorization_header)
        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
