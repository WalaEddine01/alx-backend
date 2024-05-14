#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel
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





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
