#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
"""


from flask import Flask, render_template
from models import storage
from models import state

app = Flask(__name__, template_folder="./templates")

@app.route('/states_list', strict_slashes=False)
def state_html():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template("7-states_list.html", states = storage.all("State"))

@app.teardown_appcontext()
def teardown(exc):
    """_summary_

    Args:
        exc (_type_): _description_
    """
    storage.close()


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)