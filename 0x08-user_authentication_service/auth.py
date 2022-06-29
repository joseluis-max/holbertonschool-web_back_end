#!/usr/bin/env pyth3
""" define a _hash_password method that takes
    in a password string arguments and returns bytes.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
from uuid import uuid4
from typing import Union


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register an User if doesn't exist """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """ Credentials validation """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str):
        """  returns the session ID as a string. """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ It takes a single session_id string
            argument and returns the corresponding User or None.
        """
        if session_id is None:
            return None
        else:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except NoResultFound:
                return None

    def destroy_session(self, user_id: int) -> None:
        """ Destroy a session """
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """ get_reset_password_token """
        try:
            user = self._db.find_user_by(email=email)
            token: str = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update password """
        try:
            usr = self._db.find_user_by(reset_token=reset_token)
            self._db.update_user(usr.id, password=_hash_password(password),
                                 reset_token=None)
        except NoResultFound:
            raise ValueError

    @property
    def db(self):
        """ Dababase """
        return self._db


def _hash_password(password: str) -> bytes:
    """ salted hash of the input password, hashed with bcrypt.hashpw. """
    import bcrypt

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Return a string representation of a new UUID. """
    return str(uuid4())
