from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

import os, sys, subprocess

# import custom file
from constants import Constants

app = Flask(__name__, static_url_path=None)

app.static_url_path='/templates/static'

app.static_folder = app.root_path + app.static_url_path

# ----------------------------------------- #
# databse configuration start
# declare db connection
db = SQLAlchemy(app)

# migate database
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# database models
from db_config import DB_Config

# database configuration stop
# ------------------------------------------ #

from routes import Routes

if __name__ == '__main__':
	# if you want to migrate database, uncomment the below text
	# manager.run()

	app.run(host='0.0.0.0', port=80, debug=True)