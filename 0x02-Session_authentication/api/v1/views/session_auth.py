#!/usr/bin/env python3
"""New view for Session Authentication
"""

from flask import jsonify, request, make_response
from models.user import User
from api.v1.app import auth


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

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)
    return response


@app.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """method to destroy session"""
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
