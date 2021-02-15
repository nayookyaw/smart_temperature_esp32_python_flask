from __main__ import app, db

class DB_Config:

  db_username = 'root'
  db_password = 'root'
  db_name = 'revolution'

  # db config
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+ db_username +':' + db_password + '@localhost/' + db_name
  app.config['SQLALCHEMY_ECHO'] = True
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.init_app(app)

  # import database models
  import Models.Images
  # import Models.Logs

  # run database for tables
  with app.app_context():
    db.create_all()