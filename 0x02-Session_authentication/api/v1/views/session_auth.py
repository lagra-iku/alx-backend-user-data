#!/usr/bin/env python3
"""New view for Session Authentication
"""

from flask import jsonify, request, make_response, abort
from models.user import User
from api.v1.views import app_views
from os import getenv


@app.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """method for new view for session authentication
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            user_id = u.id
            from api.v1.app import auth
            session_id = auth.create_session(user_id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return response
        else:
            return jsonify(error="wrong password"), 401
    return jsonify(error="no user found for this email"), 404   


@app.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """method to destroy session"""
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
