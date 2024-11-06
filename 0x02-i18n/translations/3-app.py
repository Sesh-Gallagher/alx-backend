#!/usr/bin/env python3
"""
Module for a Basic flask application
"""
from flask import request
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config:
    """
    Represents  application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app = Flask(__name__)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """
    Represents a function that renders a basic html template
    """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """
    Represents function that gets locale from request object
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
