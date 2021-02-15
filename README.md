# required modules

$ pip3 install flask
$ pip3 install flask_sqlalchemy
$ pip3 install mysqlclient
$ pip3 install flask_script
$ pip3 install flask_migrate
$ pip3 install boto3

# Reference
Migrate Database Guide
https://flask-migrate.readthedocs.io/en/latest/

$ python3 server.py db init
$ python3 server.py db migrate
$ python3 server.py db upgrade
$ python3 server.py db --help