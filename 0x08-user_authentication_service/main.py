#!/usr/bin/env python3
"""Test module for the API"""

import requests


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """register_user function"""
    response = requests.post(
        'http://localhost:5000/users',
        data={'email': email, 'password': password}
    )

    assert response.status_code == 200

    expected_str = '{"email":"' + email + '","message":"user created"}\n'
    assert response.content == expected_str.encode()


def log_in_wrong_password(email: str, password: str) -> None:
    """log_in_wrong_password function"""
    response = requests.post(
        'http://localhost:5000/users',
        data={'email': email, 'password': password}
    )

    assert response.status_code == 400

    expected_str = b'{"message":"email already registered"}\n'
    assert response.content == expected_str


def profile_unlogged() -> None:
    """profile_unlogged function"""
    response = requests.get(
        'http://localhost:5000/profile',
        cookies={'session_id': "nope"}
    )

    assert response.status_code == 403

    expected_str = b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 \
Final//EN">\n<title>403 Forbidden</title>\n<h1>Forbidden</h1>\
\n<p>You don\'t have the permission to access the \
requested resource. It is either read-protected \
or not readable by the server.</p>\n'
    assert response.content == expected_str


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
