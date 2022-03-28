from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def index():
    return render_template("home.html")

@views.route("/createAlert")
def createAlert():
    return render_template("createAlert.html")