from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    country = SelectField('Country', choices=[
       ('GHS', 'Ghana'),
        ('USD', 'United States'),
        ('EUR', 'Eurozone'),
        ('JPY', 'Japan'),
        ('GBP', 'United Kingdom'),
        ('NGN', 'Nigeria'),
        ('DOP', 'Dominican Republic'),
        ('CAD', 'Canada'),
        ('CHF', 'Switzerland'),
        ('ZAR', 'South Africa'),
        ('OTHER', 'Other')])
    submit = SubmitField('Sign Up')
    