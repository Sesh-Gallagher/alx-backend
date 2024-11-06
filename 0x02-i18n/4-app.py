#!/usr/bin/env python3
"""
Module for a basic flask application
"""
from flask import Flask
from flask import request
from flask_babel import Babel
from flask import render_template


class Config:
    """
    Represents application config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """
    Represents function for  a basic html template
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """
    Represents function to get locale from request object
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
