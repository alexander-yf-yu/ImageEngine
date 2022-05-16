from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from google.cloud import firestore
from werkzeug.utils import secure_filename
import os

from .forms import ImageUploadForm

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOADS_DEFAULT_DEST'] = '/var/uploads'
app.config['UPLOADS_DEFAULT_URL'] = '/var/uploads'
Bootstrap(app)

# using service account in environment
# db = firestore.Client()
db = firestore.Client.from_service_account_json("shopify-data-gcr-key.json")

collection_name = os.environ['COLLECTION_NAME']
image_dir = os.environ['IMAGE_DIR']

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = ImageUploadForm()

    if form.validate_on_submit():
        f = form.image.data
        f.save(os.path.join(image_dir, secure_filename(f.filename)))
        #img_ref = db.collection(collection_name).document(secure_filename(file.filename))
        #data = {
        #        u'description': 'asdf',
        #        }
        #img_ref.set(data)
        return redirect(url_for('hello_world'))
    else:
        return render_template('upload.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


