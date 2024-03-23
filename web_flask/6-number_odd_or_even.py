#!/usr/bin/python3
"""
starts a Flask web application:

    Returns:
        string: in html form.
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates')


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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pymagic(text):
    """
    functions gets called when user inputs '/python/<anytext>'

    Returns:
        String : HTML
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def converter(n):
    """
    functions gets called when user inputs '/number/n'

    Returns:
        String : if n is int otherwise 404 page
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numhtml(n):
    """
    functions gets called when user inputs '/number/n'

    Returns:
        String : if n is int otherwise 404 page
    """
    return render_template('5-number.html', num=n, title='HBNB')


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """
    functions gets called when user inputs '/number/n'

    Returns:
        String : if n is int otherwise 404 page
    """
    return render_template('6-number_odd_or_even.html', num=n, title='HBNB')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
