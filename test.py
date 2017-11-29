@app.route("/auth", methods=["GET","POST"])
def auth():
    try:
        username = request.form['User']
        password = request.form['Pass']
        if util.db_builder.auth_user(username,password):
            session['username'] = username
            session['password'] = password
            return redirect(url_for('profile'))
        else:
            print "invalid user/pass combo" #testing purposes
            return redirect(url_for('home'))
    except:
        return redirect(url_for('home'))


@app.route("/profile")
def profile():
    if "username" not in session:
        return redirect(url_for("home"))
    else:
        return render_template("profile.html")
