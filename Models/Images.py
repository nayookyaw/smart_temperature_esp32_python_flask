from __main__ import db

class Images(db.Model):
  """ Data model for images """

  __tablename__ = 'images'
  
  id = db.Column(
    db.Integer,
    primary_key = True
  )
  name = db.Column(
    db.String(80),
    index = False,
    unique = False,
    nullable= False
  )
  uuid = db.Column(
    db.String(120),
    index = True,
    unique = False,
    nullable = False
  )
  is_approved = db.Column(
    db.String(64),
    index = False,
    unique = False,
    nullable = True
  )
  created_at = db.Column(
    db.DateTime,
    index = True,
    unique = False,
    nullable = True
  )
  deleted_at = db.Column(
    db.DateTime,
    index = True,
    unique = False,
    nullable = True
  )

  def __repr__(self):
    return '<Images {}>'.format(self.name)
