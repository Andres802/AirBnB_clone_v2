#!/usr/bin/python3
"""
Function that starts a Flask web application
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def sayHello():
    """Function to say hello"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def sayHello2():
    """Function to say hello"""
    return 'HBNB'


@app.route('/c/<var>')
def anotherRoute(var):
    """C is magic"""
    return 'C {}'.format(var.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """Python is cool"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def isInt(n):
    """return int if n is a number , casted with int"""
    return "{} is anumber".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """retrurn if it is an int"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def render_template2(n):
    """Return if number is odd or even"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)
