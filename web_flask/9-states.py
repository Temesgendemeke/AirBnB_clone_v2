#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder="./templates")


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """_summary_

    Returns:
        _type_: _description_
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states, id=id)


@app.teardown_appcontext
def teardown(exc):
    """_summary_

    Args:
        exc (_type_): _description_
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
