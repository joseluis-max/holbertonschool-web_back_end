#!/usr/bin/env python3
""" Basic auth module
"""
from auth import Auth
import re


class BasicAuth(Auth):
    """ BasicAuth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Base64 part of the Authorization header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        match = re.match(r'^Basic ', authorization_header)
        if match is None:
            return None
        else:
            split = authorization_header.split(' ')
            authorization_header = ' '.join(split[1:])
            return authorization_header
