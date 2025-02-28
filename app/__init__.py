from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Initialize necessary classes
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))


def create_app():
    # Create app
    app = Flask(__name__, template_folder="templates",
                static_folder="static")

    # Configuration of the database (DO NOT CHANGE)
    app.config['SECRET_KEY'] = b'\xdb9#\x07(B\xcb\xa5\x1d\xf6\xec&'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    login_manager.login_view = 'auth.login'

    # Bind the database to the app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints
    from .main import bp as main_bp # noqa: E402
    app.register_blueprint(main_bp)

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp) # noqa: E402

    with app.app_context():
        from . import models  # Import models so they are registered

    return app
