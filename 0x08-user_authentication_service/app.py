#!/usr/bin/env python3
""" Flask app """
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', method=["GET"])
def home():
    return jsonify({"message": "Bienvenue"})


@app.route('/user', method=["POST"], strict_slashes=False)
def user():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": {}, "message": "user created".format(email)}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', method=["GET"], strict_slashes=False)
def session():
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        response = make_response({"email": {}, "message": "logged in".format(email)})
        response.set_cookie('session_id', session_id)
        return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
