#!/usr/bin/env python3
"""A module for the Session Authentication class.
"""

from uuid import uuid4
from flask import request
from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """class SessionAuth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """A method to create a Session ID for a user"""
        if user_id is None or not isinstance(user_id, str):
            return None
        
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
