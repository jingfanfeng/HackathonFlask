from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes import bp as main_bp

# Initialize SQLAlchemy (without binding to an app yet)
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # Create app
    app = Flask(__name__, template_folder="../templates",
                static_folder="../static")

    # Configuration of the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind the database to the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(main_bp)

    with app.app_context():
        from . import routes, models  # Import routes and models so they are registered

    return app
