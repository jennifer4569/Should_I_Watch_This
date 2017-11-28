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
            print "movie not in database"
            omdb_info = api.omdb_info(movie)
            description = omdb_info['Plot']
            reviews = ''
            recommendation = ''
            rating = omdb_info['imdbRating']
            print "I am here"
            #print movie,description,reviews,recommendation,rating
            util.db_builder.add_movie(movie,description,reviews,recommendation,rating)
            print "movie now in database"
        TITLE = movie
        #NYT API-------------------------------------------------
        nyt_info = api.nyt_info(movie)
        print "is in nyt"
        print nyt_info
        nyt_results = nyt_info['results']
        print nyt_results
        NYT_link = nyt_results[0]['link']['url']
        print NYT_link
        NYT_desc = nyt_results[0]['link']['suggested_link_text']
        print NYT_desc
        #--------------------------------------------------------
        print "stuff"
        #OMDB API-----------------------------------------------=
        omdb_info = api.omdb_info(movie)
        print "is in omdb"
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
