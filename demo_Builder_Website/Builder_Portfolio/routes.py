from flask import render_template, redirect, url_for
from Builder_Portfolio import app

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("home"))

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")