#!/usr/bin/env python3
"""A module for the Session Authentication class.
"""

from uuid import uuid4
from flask import request
from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    pass
