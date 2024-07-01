"""docstring here"""
import os


class Config:
    """Base configuration."""
    SECRET_KEY = 'supersecretkey' or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_ECHO = False
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///prod.db'


config_by_name = dict(
    development=DevelopmentConfig,
    test=TestingConfig,
    production=ProductionConfig
)
