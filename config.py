import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///urls.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
    CELERY_BROKER_URL = REDIS_URL
