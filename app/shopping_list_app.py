from flask import Flask, render_template, redirect, url_for, request

app = Flask (__name__)

@app.route('/')
def index():
    return render_template("sign_up.html")

@app.route('/login')
def login():
    return render_template("sign_in.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/sign_in', methods = ['POST'])
def sign_in():
    return redirect(url_for('dashboard'))

@app.route('/sign_up', methods = ['POST'])
def sign_up():
    return redirect(url_for('dashboard'))


if __name__=='__main__':
    app.run(debug = True, port = 8000,host='0.0.0.0')
