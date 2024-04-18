#!/usr/bin/env python3
"""A module for the Session Authentication class.
"""

from api.v1.views import app_views
from api.v1.auth.auth import Auth
from flask import abort, jsonify, request
from models.user import User
import os
from typing import Tuple


class SessionAuth(Auth):
    pass
