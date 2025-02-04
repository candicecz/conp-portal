# -*- coding: utf-8 -*-
"""Froms Module

Module that contains the Form definitions

"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class SignInForm(FlaskForm):
    """
        The SignIn Form Class

        This class provides the elements to render the form for login
    """
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class SignUpForm(FlaskForm):
    """
        This SignUp Form is for new user registrations
    """
    username = StringField('Username:', validators=[DataRequired()])
    orcid = StringField('ORCID ID (Optional):')
    affiliation = StringField('Affiliation:', validators=[DataRequired()])
    pi = BooleanField('I am a Principal Investigator (PI).', false_values=(False, 'false'))
    email = StringField('Email:', validators=[DataRequired()])
    password1 = PasswordField('Password:', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password:', validators=[DataRequired()])
    tos = BooleanField(' I have read and agree to the Terms of Use and Privacy Policy.',
                       validators=[DataRequired()])
    submit = SubmitField('Register')
