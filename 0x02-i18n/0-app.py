#!/usr/bin/env python3
"""
Module for a Basik Flask app.
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def get_index() -> str:
    """
    Represents and renders a basic home/index html page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
