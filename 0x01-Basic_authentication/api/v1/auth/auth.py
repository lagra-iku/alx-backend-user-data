#!/usr/bin/env python3
""" Module of the auth Class
"""

import re
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method require_auth"""
        if path is None or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if (excluded_path.endswith('*') and
                    path.startswith(excluded_path[:-1])):
                return False
            elif path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Method authorization header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Method current user"""
        return None
