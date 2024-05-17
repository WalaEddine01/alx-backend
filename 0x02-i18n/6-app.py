#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    Returns a user dictionary or None if ID value can't be found
    or if 'login_as' URL parameter was not found
    """
    id = request.args.get('login_as', None)
    if id and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    Add user to flask.g if user is found
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    Select and return best language match based on supported languages
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    if g.user:
        loc = g.user.get('locale')
        if loc and loc in app.config['LANGUAGES']:
            return loc
    loc = request.headers.get('locale', None)
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index():
    """
    The get_index method
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
