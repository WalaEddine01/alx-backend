#!/usr/bin/env python3
"""
Basic Flask app
"""
from locale import getlocale
from flask import Flask, render_template
from flask_babel import Babel
from flask import request
app = Flask(__name__)


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello_world():
    """
    The get_index method
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
