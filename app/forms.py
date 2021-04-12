from wtforms.validators import DataRequired
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_wtf import FlaskForm


class UploadForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])

