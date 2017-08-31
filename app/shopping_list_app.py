from flask import Flask 
from flask import render_template

app = Flask (__name__)

@app.route('/')
@app.route('/<name>')
def index(name='Peter'):
    return render_template("sign_up.html")

if __name__=='__main__':
    app.run(debug = True, port = 8000,host='0.0.0.0')
