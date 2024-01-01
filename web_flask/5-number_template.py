#!/usr/bin/python3
"""
Starts a Flask web application.
Listens on port 0.0.0.0, port 5000
"""
from flask import Flask, escape, render_template

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


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text='is_cool'):
    """
    Displays 'Python' followed by the value of <text>.
    Default is 'Python is cool'
    """
    return 'Python ' + escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """ Displays '<value of n> is a number' """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number_template(n):
    """ Displays a HTML page only if n is an integer """
    return render_template('number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
