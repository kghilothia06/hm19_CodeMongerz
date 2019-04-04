from flask_wtf import FlaskForm
from wtforms  import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators  import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class GetMedicineForm(FlaskForm):
    firstname = StringField('First Name',validators=[DataRequired(), Length(min=2,max=20)])
    lastname = StringField('Last Name',validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phoneNo = StringField('PhoneNo', validators=[DataRequired(), Length(min=10, max=13)])
    upload = FileField('Prescription')
    submit = SubmitField('Submit')