from services.serve import app
from flask import render_template,session,flash,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField

class SimpleForm(FlaskForm):

    breed = StringField('What breed are you ?')
    submit = SubmitField('Please click on me!')

@app.route('/',methods=['GET','POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        flash(f"breed change : {session['breed']}")
        return redirect(url_for('index'))
    return render_template('index.html',form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
