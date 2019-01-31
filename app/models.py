from datetime import datetime
from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    vid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    sex = db.Column(db.Integer)
    institution = db.Column(db.String(100))
    school = db.Column(db.Boolean)
    status = db.Column(db.Integer)
    time_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    lastseen = db.Column(db.DateTime)

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def super(self):
        return self.email=="nandujkishor@gmail.com"