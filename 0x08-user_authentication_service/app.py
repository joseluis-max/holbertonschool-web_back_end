#!/usr/bin/env python3
"""Set up a basic Flask app
"""
from auth import Auth
from flask import Flask, jsonify, request, abort, make_response, redirect


AUTH = Auth()
app = Flask(__name__)


@app.route("/")
def home():
    """Home route
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", method=["POST"], strict_slashes=False)
def user():
    """ User registration """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": {}, "message":
                        "user created".format(email)}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", method=["GET"], strict_slashes=False)
def login():
    """ Login """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        response = make_response({"email": {}, "message":
                                  "logged in".format(email)})
        response.set_cookie('session_id', session_id)
        return response


@app.route("/sessions", method=["DELETE"], strict_slashes=False)
def logout():
    """ Log out """
    session_id = request.cookies.get('session_id')
    usr = AUTH.get_user_from_session_id(session_id)
    if usr is None:
        return 403
    else:
        AUTH.destroy_session(usr.id)
        return redirect('/')


@app.route("/profile", method=["GET"], strict_slashes=False)
def profile():
    """ profile """
    session_id = request.cookies.get('session_id')
    usr = AUTH.get_user_from_session_id(session_id)
    if usr:
        return jsonify({"email": "{}".format(usr.email)}), 200
    else:
        return 403.


@app.route("/reset_password", method=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ get reset password token """
    email = request.form.get('email')
    usr = AUTH.db.find_user_by(email=email)
    if usr:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": "{}".format(email),
                        "reset_token": "{}".format(token)}), 200
    else:
        return 403


@app.route("/reset_password", method=['PUT'], strict_slashes=False)
def update_password():
    """ update password """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    try:
        usr = AUTH.db.find_user_by(email=email)
        if usr.reset_token == reset_token:
            AUTH.update_password(reset_token, new_password)
            return jsonify({"email": "{}".format(email),
                            "message": "Password updated"}), 200
    except Exception:
        return 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
