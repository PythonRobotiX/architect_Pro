from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from .config import Config  # Ensure this import is correct

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
    # Import other blueprints as necessary

    app.register_blueprint(auth_bp)
    app.register_blueprint(contact_bp)
    # Register other blueprints as necessary

    return app
