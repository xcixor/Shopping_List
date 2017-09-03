from flask import Flask, render_template, redirect, url_for, request

from myapp import APP

@APP.route('/')
def index():
    return render_template("sign_up.html")

@APP.route('/login')
def login():
    return render_template("sign_in.html")

@APP.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@APP.route('/sign_in', methods = ['POST'])
def sign_in():
    return redirect(url_for('dashboard'))

@APP.route('/sign_up', methods = ['POST'])
def sign_up():
    return redirect(url_for('dashboard'))

