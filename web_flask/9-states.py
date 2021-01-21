#!/usr/bin/python3
""" Module docstring """


from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """ Close session """
    storage.close()


@app.route('/states')
@app.route('/states/<id>')
def state_and_state(id=None):
    """ Display HTML with  STATES
        or  CITIES with specific id """
    state = ''
    states = storage.all(State)
    if id:
        key = "State." + id
        if key in states.keys():
            state = states[key]
    return render_template('9-states.html', id=id, state=state, states=states)
