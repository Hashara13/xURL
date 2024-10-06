from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from celery import Celery
from urls import routes
from xURL import app, db

app=Flask(__name__)
app.config.from_object('config.Config')

db=SQLAlchemy(app)
cache=Cache(app)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])

if __name__ == "__main__":
    app.run()