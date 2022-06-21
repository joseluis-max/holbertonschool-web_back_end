#!/usr/bin/env python3
""" Authentication module
"""
from flask import flask, request
from typing import List, TypeVar


class Auth():
    """ Auth Class
    """

    # fix both with slash and without slash
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Requre auth
        """
        if path is None or excluded_paths is None:
            return True
        if len(excluded_paths) == 0:
            return True
        if path not in excluded_paths:
            return True
        else:
            return False
    
    def authorization_header(self, request=None) -> str:
        """ Authorization_header
        """
        if request is None:
            return None
        try:
            value = request.get('Authorization')
            return  value
        except KeyError:
            return None 
        

    def current_user(self, request=None) -> TypeVar('User'):
        return None
