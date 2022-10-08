from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators
class newsLetter(FlaskForm):
    nameField = StringField('name', [validators.Length(min=1)])
    emailField = StringField('E-mail', [validators.Length(min=6, max=35)])
    submit = SubmitField('Sign me up')

app = Flask(__name__)
app.secret_key="akdhlgadi342"
@app.route('/')
def get_home():
    form = newsLetter()
    
    return render_template('index.html', title='Home', form=form)