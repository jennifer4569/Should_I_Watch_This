import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O
import os #Used for os.remove()

f="util/moviematchers.db"
g = "moviematchers.db"
try:
    os.remove(f) #Used During Testing to remove file at the beginning
except:
    print "database does not exist" 

def create_db():
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "CREATE TABLE users(id INTEGER, username TEXT, password TEXT, liked_movies TEXT, search_history TEXT)"
    c.execute(command)
    #command = "INSERT INTO users VALUES(1,'ibnul','ibnul','ibnul','ibnul')"
    #c.execute(command)
    command = "CREATE TABLE movies(name TEXT, overview TEXT, reviews TEXT, recommendations TEXT, ratings REAL)"
    c.execute(command)
    db.commit()
    db.close()

def add_user(username, password):
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "SELECT id FROM users ORDER BY id DESC"
    c.execute(command)
    id = c.fetchone()
    if (id == None):
        id = 0
    else:
        id = id[0] +1
    command = "INSERT INTO users VALUES(" + str(id) + ",'" + username + "','" + password + "','','')"
    c.execute(command)
    db.commit()
    db.close()

def add_movie(name,description,reviews,recommendation,rating):
    #reviews = omdb_info['Plot']
    #recommendation = omdb_info['Plot']
    db = sqlite3.connect(f)
    c = db.cursor()
    #command = "INSERT INTO movies VALUES('" + name + "','This is a description','Wonderful.,cool!','The Dark Knight, Pokemon',4.78)"
    #add_user("ji","jey")
    print "oeisnhriog"
    command = 'INSERT INTO movies VALUES("' + name + '","' + description + '","' + reviews + '","' + recommendation + '",' + str(rating) + ')'
    #" + str(rating) + "
    c.execute(command)
    db.commit()
    db.close()

def check_movie(name):
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "SELECT name FROM movies"
    movies = []
    for row in c.execute(command):
        movies.append(row[0])
    if name in movies:
        return True
    else:
        return False

def auth_user(username,password):
    db = sqlite3.connect(f)
    c = db.cursor()
    command = "SELECT username,password FROM users"
    d = {}
    for row in c.execute(command):
        d[row[0]] = row[1]
    if username in d:
        if d[username] == password:
            return True
        else:
            return False
    else:
        return False
    db.commit()
    db.close()


create_db()
#add_user("hi","hey")
#add_movie("The Dark Knight Rises")
