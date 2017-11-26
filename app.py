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
        #NYT API-------------------------------------------------
        nyt_info = api.nyt_info(movie)
        nyt_results = nyt_info['results']
        NYT_link = nyt_results[0]['link']['url']
        NYT_desc = nyt_results[0]['link']['suggested_link_text']
        #--------------------------------------------------------

        #OMDB API-----------------------------------------------=
        omdb_info = api.omdb_info(movie)
        DIRECTOR = omdb_info['Director']
        PLOT = omdb_info['Plot']
        ACTORS = omdb_info['Actors']
        POSTER = omdb_info['Poster']
        #--------------------------------------------------------
        
        #tastedive_info = api.tastedive_info(movie)
        #if tastedive_info == -1:
            #TASTEDIVE = "No similar results found"
        #else:
            #results = tastedive_info['Results']
        return render_template("display.html", title = TITLE, review_link = NYT_link, review_title = NYT_desc, \
                               director = DIRECTOR, actors = ACTORS, plot = PLOT, poster = POSTER)
    except:
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()
