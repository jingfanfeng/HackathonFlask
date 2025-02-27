from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .routes import bp as main_bp

# Initialize SQLAlchemy (without binding to an app yet)
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    # Create app
    app = Flask(__name__, template_folder="../templates",
                static_folder="../static")

    # Configuration of the database (DO NOT CHANGE)
    app.config['SECRET_KEY'] = b'\xdb9#\x07(B\xcb\xa5\x1d\xf6\xec&'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind the database to the app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)

    with app.app_context():
        from . import routes, models  # Import routes and models so they are registered

    return app
