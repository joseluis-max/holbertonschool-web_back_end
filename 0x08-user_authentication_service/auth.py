#!/usr/bin/env pyth3
""" define a _hash_password method that takes
    in a password string arguments and returns bytes.
"""
import bcrypt

from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
from uuid import uuid4


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
            return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False


def _hash_password(password: str) -> bytes:
    """ salted hash of the input password, hashed with bcrypt.hashpw. """
    import bcrypt

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Return a string representation of a new UUID. """
    return str(uuid4())
