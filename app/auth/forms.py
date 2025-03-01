from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo, Length, Regexp, ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log In')


def password_custom_length_validator(form, password_field):
    if len(password_field.data) < 8:
        raise ValidationError("Password must be at least 8 characters long")


class SignupForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[
        InputRequired(),
        password_custom_length_validator,
        Regexp(
            r".*[A-Z].*", message="Password must contain at least one uppercase letter"),
        Regexp(
            r".*[a-z].*", message="Password must contain at least one lowercase letter"),
        Regexp(r".*[0-9].*", message="Password must contain at least one digit"),
        Regexp(r".*[^A-Za-z0-9].*",
               message="Password must contain at least one special character"),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', validators=[
                            InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
