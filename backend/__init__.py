from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from config import Config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    from .routes.auth_routes import auth_bp
    from .routes.contact_routes import contact_bp
    from .routes.portfolio_routes import portfolio_bp
    from .routes.thesis_routes import thesis_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(portfolio_bp)
    app.register_blueprint(thesis_bp)

    return app
