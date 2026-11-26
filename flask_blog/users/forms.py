from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flask_blog.models import User


class RegistrationForm(FlaskForm):
  username = StringField(label="Username", validators=[DataRequired(), Length(min=3, max=20)])
  email = StringField(label="Email", validators=[DataRequired(), Email()])
  password = PasswordField(label="Password", validators=[DataRequired()])
  confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo("password")])
  submit = SubmitField("Sign Up")

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first() or None
    if user: 
      raise ValidationError("That username is taken. Please choose another one.")
  
  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first() or None
    if user: 
      raise ValidationError("That email is taken. Please choose another one.")


class LoginForm(FlaskForm):
  email = StringField(label="Email", validators=[DataRequired(), Email()])
  password = PasswordField(label="Password", validators=[DataRequired()])
  remember = BooleanField(label="Remember Me")
  submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
  username = StringField(label="Username", validators=[DataRequired(), Length(min=3, max=20)])
  email = StringField(label="Email", validators=[DataRequired(), Email()])
  picture = FileField(label="Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
  submit = SubmitField("Update")

  def validate_username(self, username):
    if username.data != current_user.username:
      user = User.query.filter_by(username=username.data).first() or None
      if user: 
        raise ValidationError("That username is taken. Please choose another one.")
  
  def validate_email(self, email):
    if email.data != current_user.email:
      user = User.query.filter_by(email=email.data).first() or None
      if user: 
        raise ValidationError("That email is taken. Please choose another one.")


class RequestResetForm(FlaskForm):
  email = StringField(label="Email", validators=[DataRequired(), Email()])
  submit = SubmitField("Request Password Reset")

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first() or None
    if user is None: 
      raise ValidationError("There is no account with this email. Register first.")


class ResetPasswordForm(FlaskForm):
  password = PasswordField(label="Password", validators=[DataRequired()])
  confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo("password")])
  submit = SubmitField("Reset Password")

