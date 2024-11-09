import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_jwt_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql+pymysql://user:password@localhost/your_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300
    RATELIMIT_DEFAULT = "100 per day"

config = Config()
