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
babel._configure_jinja = False


@app.route('/')
def get_index():
    """
    The get_index method
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    the get_local method
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(
        map(
            lambda x: (x if '=' in x else '{}='.format(x)).split('='),
            queries,
            ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
