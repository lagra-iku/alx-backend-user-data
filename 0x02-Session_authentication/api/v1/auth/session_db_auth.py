#!/usr/bin/env python3
"""Module for destroying a session
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """Class for session db auth
    """
    def create_session(self, user_id=None):
        """method to create session"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        user_session = UserSession(user_id=user_id, session_id=session_id)
        db_session.add(user_session)
        db_session.commit()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """method to user id per session"""
        if session_id is None:
            return None

        user_session = UserSession.query.filter_by(
                session_id=session_id).first()
        if user_session is None:
            return None
        return user_session.user_id

    def destroy_session(self, request=None):
        """method to destroy session"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_session = UserSession.query.filter_by(
                session_id=session_id).first()
        if user_session is None:
            return False

        db_session.delete(user_session)
        db_session.commit()
        return True
