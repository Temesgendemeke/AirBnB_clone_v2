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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
