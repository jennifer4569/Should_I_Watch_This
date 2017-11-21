#!usr/bin/python

from flask import Flask, session, render_template, request, redirect, url_for, flash

@app.route("/")
def landing():
    return "hello"

if __name__ == "__main__":
    app.debug = True
    app.run()
