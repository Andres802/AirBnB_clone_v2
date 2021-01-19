#!/usr/bin/python3
"""
Scripts that creates a server with flask framework
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def sayHello():
    """Function that reply back say hello"""
    return "Hello HBNB"


@app.route("/hbnb")
def sayHello2():
    """Function tha reply back HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def sayHello3(text):
    """Function that reply back C is $"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
