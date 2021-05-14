from services.serve import app
from flask import render_template,flash, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField

class SimpleForm(FlaskForm):

    submit = SubmitField('Please click on me!')

@app.route('/',methods=['GET','POST'])
def index():
    form = SimpleForm()

    if form.validate_on_submit():
        flash('just click the button')

        return redirect(url_for('index'))
    return render_template('index.html',form=form)

@app.route('/test')
def test():
    return 'test'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
