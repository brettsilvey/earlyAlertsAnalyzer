from flask import Flask
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "helloworld"

    db = MongoClient('localhost', 27017)
    myDatabase = db.EarlyAlerts
    myCollection = myDatabase.UnfilteredAlerts

    from .views import views

    app.register_blueprint(views, url_prefix="/")


    return app