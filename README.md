/*
    Developed by Nay Oo Kyaw
    nayookyaw.nok@gmail.com
*/

# Required modules

$ pip3 install flask <br>
$ pip3 install flask_sqlalchemy <br>
$ pip3 install flask_script <br>
$ pip3 install flask_migrate <br>
$ pip3 install boto3 <br>


# Install Mysql Server in Linux
https://linuxize.com/post/how-to-install-mysql-on-ubuntu-18-04/

$ sudo apt install mysql-server
(Need to put database new password during installation and configuration)


https://stackoverflow.com/questions/53641541/why-pip-install-mysqlclient-not-working-in-ubuntu-18-04-lts/53641741

# Replace python3.9 with which ever version of Python3 you are using
sudo apt-get install python3.6-dev 
sudo apt-get install mysql-client
sudo apt-get install libmysqlclient-dev
sudo apt-get install libssl-dev

$ pip3 install mysqlclient <br>

# Reference
Migrate Database Guide
https://flask-migrate.readthedocs.io/en/latest/

$ python3 server.py db init <br>
$ python3 server.py db migrate <br>
$ python3 server.py db upgrade <br>
$ python3 server.py db --help <br>