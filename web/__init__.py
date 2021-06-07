from flask import Flask,blueprints
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

# Create app function to create app
def create_app():
    from .view import view
    from .auth import auth
    from .models import User, Students, Classs

    app = Flask(__name__)

    app.config['SECRET_KEY'] = '*$@&*(%@(*YHFRUFHOWUHO*@$(FHSUkgfauguo$@&*(%@(*YHFRUFHOWUHO*@$(FHSUkgfauguoaaaaaaaaaaaaaaaaaaaaaaassssss'# for session
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    app.register_blueprint(view, url_prefix='/')# added blueprint of view.py to show the page
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('web/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
