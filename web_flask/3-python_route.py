#!/usr/bin/python3
"""
starts a Flask web application:

    Returns:
        string: in html form.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    functions gets called when user inputs ip or domain name + '/'

    Returns:
        String : HTML
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hellosec():
    """
    functions gets called when user inputs '/hbnb'

    Returns:
        String : HTML
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    functions gets called when user inputs '/c/<anytext>'

    Returns:
        String : HTML
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text':'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pymagic(text):
    """
    functions gets called when user inputs '/python/<anytext>'

    Returns:
        String : HTML
    """
    return "python {}".format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
