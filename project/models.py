from email.policy import default
from flask_security import UserMixin, RoleMixin
from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, backref
import uuid
from . import db


### Role and User relations

class RolesUsers(db.Model, RoleMixin, UserMixin):
    __tablename__ = 'roles_users'
    id = db.Column(db.Uuid(), primary_key=True, nullable=True, default=uuid.uuid4())
    user_id = db.Column('user_id', db.Uuid(), ForeignKey('users.id'))
    role_id = db.Column('role_id', db.Uuid(), ForeignKey('roles.id'))
    @hybrid_property
    def fs_uniquifier(self):
        return self.id

### USER

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Uuid, primary_key=True, default=uuid.uuid4()) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    created_at = db.Column(db.DateTime())
    is_active = db.Column(db.Boolean())
    roles = relationship('Role', secondary='roles_users',
    backref=backref('users', lazy='dynamic'))

    @hybrid_property
    def fs_uniquifier(self):
        return self.id

    def __repr__(self):
        return f'<User {self.email}>'

### ROLE

class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Uuid, primary_key=True, default=uuid.uuid4()) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(80), unique=True)
    @hybrid_property
    def fs_uniquifier(self):
        return self.id

    def __repr__(self):
        return f'<Role {self.name}>'