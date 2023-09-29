"""
    config classes for the application
"""

import os

class Config:
    """
        Base configuration class

        -> base configurations necessary in all Flask applications
    """

    # To generate a good random secret key string run the following two commands in a python interpreter:-
    # $ import secrets
    # $ secrets.token_urlsafe(16)
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1EZKpnQcRzHdR9wHLy7GYw'

class Development(Config):
    """
        Development class
    
        -> configurations for the application while testing in development
    """

class Production(Config):
    """
        Production class

        -> configurations for the application when deploying on production
    """

