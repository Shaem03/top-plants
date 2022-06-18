import os

# Define the application directory
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

username = os.environ.get('PSQL_USER_NAME')
password = os.environ.get('PSQL_PASSWORD')
host_name = os.environ.get('PSQL_HOST_NAME')
db_name = os.environ.get('PSQL_DB')
port = os.environ.get('PSQL_PORT')


class Config(object):
    DATABASE_CONNECT_OPTIONS = {}

    # Turn off Flask-SQLAlchemy event system
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    WTF_CSRF_ENABLED = True
    CORS_HEADERS = 'Content-Type'
    SQLALCHEMY_POOL_RECYCLE = 60


class APIConfig(Config):
    """Statement for enabling the api environment"""
    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = F'postgresql+psycopg2://{username}:{password}@{host_name}/{db_name}'
    WTF_CSRF_ENABLED = False


config = {
    'api': APIConfig,
}
