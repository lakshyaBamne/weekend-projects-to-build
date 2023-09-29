"""
    initialization file contains the application factory
"""

from flask import (
    Flask
)

# configuration class
from config import Config, Development, Production

# blueprints
from flaskr.main import bp as main_bp

def create_app():
    """
        application factory
    """

    app = Flask(__name__)

    # configuration
    app.config.from_object(Config)

    # blueprint registrations
    app.register_blueprint(main_bp)

    return app
