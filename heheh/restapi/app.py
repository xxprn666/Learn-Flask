from services.serve import app
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup_form():
    return render_template('Signup.html')

@app.route('/home')
def homepage():
    
    first= request.args.get('first')
    last = request.args.get('last')

    return render_template('HomePage.html',first=first, last=last)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
