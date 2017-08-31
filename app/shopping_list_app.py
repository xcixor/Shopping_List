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

@app.route('/save_user',methods=['POST'])
def save_user():
    return redirect(url_for("index"))

if __name__=='__main__':
    app.run(debug = True, port = 8000,host='0.0.0.0')
