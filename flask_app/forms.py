from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Optional, Length

class ImageUploadForm(FlaskForm):
    image = FileField('Your image file', validators=[FileRequired()])
    description = StringField(u'Description of image', validators=[InputRequired(), Length(min=10)])
    category = SelectField(u'Category of image', choices=[('',''), ('art', 'Art'), ('transportation', 'Transportation'), ('people', 'People'), ('tech', 'Tech'), ('nature', 'Nature')])

