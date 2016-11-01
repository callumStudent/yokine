from database import db
from flask.ext.security import UserMixin, RoleMixin

#roles_users = db.Table('roles_users',
	#db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
	#db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
	#)

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Roles_users(db.Model):
    __tablename__ = 'roles_users'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80))
    last = db.Column(db.String(80))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary= "roles_users",
	    backref=db.backref('users', lazy='dynamic'))