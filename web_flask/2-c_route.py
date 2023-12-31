#!/usr/bin/python3
"""
Starts a Flask web application.
Listens on port 0.0.0.0, port 5000
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
# Route definitions
def index():
    """ Displays Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """Displays 'C' followed by the value of <text>."""
    return 'C ' + escape(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
