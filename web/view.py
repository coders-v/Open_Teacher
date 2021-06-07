from flask import Blueprint, render_template, request, flash,redirect,url_for,session,jsonify
from flask_login import login_user, login_required, logout_user, current_user,login_manager
from .models import Classs,User
from . import db
import json

view = Blueprint('view',__name__)

@view.route('/teacher-console')
@login_required
def teachcon():
    return render_template("console.html", user=current_user)

@view.route('/')
def home():
    return render_template("home.html")


@view.route('/datas', methods = ['POST'])
def datas():
    classes = request.form['classes']
    classes = json.loads(classes)
    slass = Classs(name=classes, user_id=current_user.id)
    db.session.add(slass)
    db.session.commit() 
    return classes


@view.route('/del-class',methods=['POST'])
def delete_class():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Classs.query.filter_by(name=noteId).first()
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
