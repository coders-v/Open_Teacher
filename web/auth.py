from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User,Classs
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/signup',methods=["POST","GET"])
def signup():
    if request.method == 'POST':
        Name = request.form.get('Name')
        Email = request.form.get('Email')
        password1 = request.form.get('Password1')
        password2 = request.form.get('Password2')
        user = User.query.filter_by(email=Email).first()
        if user:
            flash('Email already exists. Login', category='error')
            return redirect(url_for('auth.login'))
        elif len(Email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(Name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=Email, name=Name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            
            return redirect(url_for('view.teachcon', user=current_user))
    return redirect(url_for("view.home"))

@auth.route('/login', methods=["POST","GET"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('view.teachcon', user=current_user))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist. SignUp', category='error')
            return redirect(url_for("view.home"))

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully',category='success')
    return redirect(url_for('auth.login'))