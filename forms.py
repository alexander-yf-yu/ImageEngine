from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SelectField, DateField
from wtforms.validators import InputRequired, Optional, Length

class ImageUploadForm(FlaskForm):
    image = FileField('Your image file', validators=[FileRequired()])
    description = StringField(u'Description of image', validators=[InputRequired(), Length(min=10)])
    pub_date = DateField('publication date')

class ImageSearchForm(FlaskForm):
    text = StringField(u'Description text', validators=[])
    start = DateField('Start date')
    end = DateField('End date')

