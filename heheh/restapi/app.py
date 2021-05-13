# from services.serve import app
# from flask import render_template, request

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/signup')
# def signup_form():
#     return render_template('Signup.html')

# @app.route('/home')
# def homepage():
#     first= request.args.get('first')
#     last = request.args.get('last')
#     return render_template('HomePage.html',first=first, last=last)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (
        StringField,
        BooleanField,
        DateTimeField,
        RadioField,
        SelectField,
        TextField,
        TextAreaField,
        SubmitField
        )
from wtforms.validators import DataRequired

app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class InfoForm(FlaskForm):

    breed = StringField('What breed are you?',validators=[DataRequired()])
    neutered  = BooleanField("Have you been neutered?")
    mood = RadioField('Please choose your mood:', choices=[('mood_one','Happy'),('mood_two','Excited')])
    food_choice = SelectField(u'Pick Your Favorite Food:',
                          choices=[('chi', 'Chicken'), ('bf', 'Beef'),
                                   ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.

        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for("thankyou"))


    return render_template('home.html', form=form)

@app.route('/thankyou')
def thankyou():

    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
