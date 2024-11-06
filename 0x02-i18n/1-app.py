#!/usr/bin/env python3
"""
Module for a Basic Flask app.
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config:
    """
    Represents tha application configuration class
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
    Represents a function that renders a basic html template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
