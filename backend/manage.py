import sys
import os

# Ensure the backend directory is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask.cli import FlaskGroup
from backend import create_app, db

app = create_app()
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
