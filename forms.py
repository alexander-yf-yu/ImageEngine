from flask_wtf import FlaskForm
from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import InputRequired, Optional, Length


images = UploadSet('images', IMAGES)

class ImageUploadForm(FlaskForm):
    image = FileField('Your image file', validators=[FileRequired(), FileAllowed(images, 'Images only!')])
    description = StringField(u'Description of image', validators=[InputRequired(), Length(min=10)])
    tag = StringField('Image tag', validators=[Optional()])
