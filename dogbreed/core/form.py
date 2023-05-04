from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
""" from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError """
from flask_wtf.file import  FileField, FileAllowed

class UpdateUserForm(FlaskForm):
    picture = FileField('Update profile picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Send')