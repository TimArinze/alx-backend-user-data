#!/usr/bin/env python3
"""
Expiration Session
"""
from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Adds Expiration date to session"""
    def __init__(self):
        """init"""
        try:
            self.session_duration = int(os.getenv("SESSION_DURATION"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """create session"""
        try:
            session_id =  super().create_session(user_id)
        except Exception:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary
        return session_id
    
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user id for session id"""
        if not session_id:
            return None
        try:
            user_id = super().user_id_for_session_id(session_id)
        except Exception:
            return None
        if not user_id:
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id].get("user_id")
        if not self.user_id_by_session_id[session_id].get("created_at"):
            return None
        duration = timedelta(seconds= self.session_duration)
        created_at = self.user_id_by_session_id[session_id].get("created_at")
        date_difference = (created_at + duration) - datetime.now

        if date_difference <= 0:
            return None
        else:
            return user_id
