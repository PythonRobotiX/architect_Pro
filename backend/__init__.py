from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    from .routes import auth_routes, contact_routes, portfolio_routes, thesis_routes
    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(contact_routes.contact_bp)
    app.register_blueprint(portfolio_routes.portfolio_bp)
    app.register_blueprint(thesis_routes.thesis_bp)

    return app
