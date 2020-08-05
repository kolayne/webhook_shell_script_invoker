import subprocess
from os import path

import flask

from config import secret_token, projects_to_scripts


app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    if flask.request.headers.get('Authorization') != secret_token:
        return flask.abort(401)
    project_name = flask.request.json.get("project_name")
    if project_name is None:
        return flask.abort(400)
    script_name = projects_to_scripts.get(project_name)
    if script_name is None:
        return flask.abort(404)
    try:
        subprocess.run([path.join('scripts/', script_name)], check=True)
    except subprocess.CalledProcessError:
        return flask.abort(500)

    return 'Ok'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2010)
