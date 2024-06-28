# backend/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config  # Use relative import

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Import parts of our application
        from .routes import auth_routes, contact_routes, portfolio_routes, thesis_routes

        # Register Blueprints
        app.register_blueprint(auth_routes.bp)
        app.register_blueprint(contact_routes.bp)
        app.register_blueprint(portfolio_routes.bp)
        app.register_blueprint(thesis_routes.bp)

    return app
