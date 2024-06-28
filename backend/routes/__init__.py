from flask import Blueprint

# Import blueprints
from .auth_routes import auth_bp
from .contact_routes import contact_bp
from .portfolio_routes import portfolio_bp
from .thesis_routes import thesis_bp

# Create a list of blueprints
blueprints = [auth_bp, contact_bp, portfolio_bp, thesis_bp]
