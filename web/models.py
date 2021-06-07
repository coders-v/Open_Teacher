from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    admission_no = db.Column(db.Integer,unique=True)
    #mark = db.Column(db.ARRAY(db.Integer,dimensions=8))
    #attendance = db.Column(db.ARRAY(db.Boolean))    
    class_id = db.Column(db.Integer, db.ForeignKey('classs.id'))

class Classs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),unique=True)
    students = db.relationship('Students')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    classes = db.relationship('Classs')
