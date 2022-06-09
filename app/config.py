import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DATABASE_CONNECT_OPTIONS = {}

    # Turn off Flask-SQLAlchemy event system
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    WTF_CSRF_ENABLED = True
    CORS_HEADERS = 'Content-Type'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'csv_test.db')


class DevelopmentConfig(Config):
    """Statement for enabling the development environment"""
    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'csv_test.db')
    DEBUG = True


class APIConfig(Config):
    """Statement for enabling the api environment"""
    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'csv_test.db')
    WTF_CSRF_ENABLED = False


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'csv_test.db')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'api': APIConfig,
}
