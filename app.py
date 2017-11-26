#!usr/bin/python

from flask import Flask, session, render_template, request, redirect, url_for, flash

import util.db_builder
import api

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET","POST"])
def search():
    try:
        movie = request.form['search']
        if util.db_builder.check_movie(movie):
            print "movie was already in database"
        else:
            util.db_builder.add_movie(movie)
        TITLE = movie
        tastedive_info = api.tastedive_info(movie)
        if tastedive_info == -1:
            TASTEDIVE = "No similar results found"
        else:
            results = tastedive_info['Results']
        return render_template("display.html", title = TITLE, recommended = results, tastedive_error = TASTEDIVE)
    except:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()
