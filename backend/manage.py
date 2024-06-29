import sys
import os

# Ensure the backend directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'backend')))

from flask.cli import FlaskGroup
from backend import create_app, db  # Import your app and db from the backend

app = create_app()
cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
