#!/usr/bin/env python3
""" Flask app """
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', method=["GET"])
def home():
    return jsonify({"message": "Bienvenue"})


@app.route('/user', method=["POST"])
def user():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": {}, "message": "user created".format(email)}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
