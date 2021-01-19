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
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
