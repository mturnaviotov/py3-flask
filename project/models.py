from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Uuid, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime())
    is_active = db.Column(db.Boolean())