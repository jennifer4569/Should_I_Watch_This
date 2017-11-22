import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os #Used for os.remove()

f="moviematchers.db"
try:
    os.remove(f) #Used During Testing to remove file at the beginning
except:
    print "Did not find table to remove"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops


def create_db():
    command = "CREATE TABLE users(id INTEGER, username TEXT, password TEXT, liked_movies TEXT, search_history TEXT)"
    c.execute(command)
    command = "INSERT INTO users VALUES(1,'ibnul','ibnul','ibnul','ibnul')"
    c.execute(command)
    command = "CREATE TABLE movie(overview TEXT, reviews REAL, recommendations TEXT, ratings TEXT)"
    c.execute(command)

create_db();

db.commit() #save changes
db.close()  #close database
