from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from config import Config

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    CORS(app)

    # Register Blueprints
    from backend.routes.auth_routes import auth_bp
    from backend.routes.contact_routes import contact_bp
    from backend.routes.portfolio_routes import portfolio_bp
    from backend.routes.thesis_routes import thesis_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(portfolio_bp)
    app.register_blueprint(thesis_bp)

    return app
