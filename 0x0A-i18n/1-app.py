#!/usr/bin/env python3
"""basic Flask app
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask("my_beautiful_app")
babel = Babel(app)


class Config():
    """configures available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/", strict_slashes=False)
def root() -> str:
    """root endpoint
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
