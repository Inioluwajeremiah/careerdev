from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
# from flask_ckeditor import ckeditor
from flask_migrate import Migrate

# db = SQLAlchemy(session_options={"autoflush": False})
db = SQLAlchemy()
migrate = Migrate()
DB_NAME = "careerdev.db"

# f'sqlite:///{DB_NAME}'
# postgres://wnvyldnupudxby:870afaf486c823c724798e5df9ea04b5b86deae769db362ae3b85b468e480f8a@ec2-44-192-245-97.compute-1.amazonaws.com:5432/d8ruv7abci36jl


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '026afd0576690d2d355d73c1adcfabd3'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///careerdev.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    # ckeditor.init_app(app)

    from .views import views
    from .auth import auth
    from .sch_post import sch_post
    from .intern import intern
    from .post_doc import post_doc
    from .ga_ast import ga_ast
    from .single_post import single_post
    from .admintop import admintop
    from .admin import admin
    from .m_search import m_search
    from .m_filter import m_filter


    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(post_doc, url_prefix="/")
    app.register_blueprint(sch_post, url_prefix="/")
    app.register_blueprint(intern, url_prefix="/")
    app.register_blueprint(ga_ast, url_prefix="/")
    app.register_blueprint(single_post, url_prefix="/")
    app.register_blueprint(admintop, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/")
    app.register_blueprint(m_search, url_prefix="/")
    app.register_blueprint(m_filter, url_prefix="/")

    @app.get('/<short_url>')
    def redirect_to_url(short_url):
        new_posts = PostModel.query.filter_by(app_short_url=short_url).first_or_404()

        if new_posts:
            new_posts.visits = new_posts.visits+1
            db.session.commit()

            return redirect(new_posts.app_url)
    from .models import PostModel, User

    create_database(app)

    loginManager = LoginManager()
    loginManager.login_view = 'auth.login'
    loginManager.init_app(app)

    @loginManager.user_loader
    def load_user(user_id):
        # (user_id)
        return models.User.query.get(int(user_id))

    return app


def create_database(app):
    if not path.exists('careerdev_package/' + DB_NAME):
        db.create_all(app=app)
        print('careerdev database created successfully')
