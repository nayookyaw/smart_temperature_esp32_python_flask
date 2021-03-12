from flask import Flask

import os, sys, subprocess

# import custom file
from constants import Constants

app = Flask(__name__, static_url_path=None)

app.static_url_path='/templates/static'

app.static_folder = app.root_path + app.static_url_path

from routes import Routes

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=33, debug=True)