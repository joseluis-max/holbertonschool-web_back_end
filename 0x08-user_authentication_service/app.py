#!/usr/bin/env python3
"""This module contains a basic Flask app
"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


AUTH = Auth()

app = Flask(__name__)


@app.route("/")
def get_request():
    """Home endpoint
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=['POST'])
def users():
    """Registers a new user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"}), 200


@app.route("/sessions", methods=["POST"])
def login():
    """Login by email and password
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    response = make_response(jsonify({
        "email": email, "message": "logged in"
    }))

    response.set_cookie('session_id', session_id)

    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """destroys the session if exists
        and redirect the user to GET '/'
    """
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect('/')


@app.route("/profile", strict_slashes=False)
def profile():
    """checks if the session_id exist and responds with 200 status
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)

    return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    """returns a token to restore password if the user exist
    """
    email = request.form.get('email')

    try:
        new_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": new_token})
    except NoResultFound:
        abort(403)


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password():
    """Updates the password. If the token is invalid
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
