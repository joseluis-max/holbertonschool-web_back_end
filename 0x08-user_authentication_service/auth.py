#!/usr/bin/env pyth3
""" define a _hash_password method that takes
    in a password string arguments and returns bytes.
"""


def _hash_password(password: str) -> bytes:
    """ salted hash of the input password, hashed with bcrypt.hashpw. """
    import bcrypt

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
