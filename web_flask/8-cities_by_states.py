#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """display a HTML page
    """
    return render_template('7-states_list.html', states=storage.all("State"))


@app.route("/cities_by_states")
def cities_by_states():
    """display a HTML page
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown_appcontext(self):
    """call storage.close()
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)