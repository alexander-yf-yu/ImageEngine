from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from google.cloud import firestore
from werkzeug.utils import secure_filename
import os

from .forms import ImageUploadForm

collection_name = os.environ['COLLECTION_NAME']
image_dir = os.environ['IMAGE_DIR']

def create_db():
    # using service account in environment
    # db = firestore.Client()
    db = firestore.Client.from_service_account_json("shopify-data-gcr-key.json")
    return db

def create_app():
    app = Flask(__name__)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    Bootstrap(app)

    db = create_db()

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        form = ImageUploadForm()

        if form.validate_on_submit():
            f = form.image.data
            img_name = secure_filename(f.filename)
            img = form.image.data
            img.save(os.path.join(image_dir, secure_filename(f.filename)))
            
            img_ref = db.collection(collection_name).document(secure_filename(f.filename))
            data = {
                u'id': img_name,
                u'description': form.description.data,
                u'category': form.category.data,
            }
            img_ref.set(data)
            return redirect(url_for('hello_world'))
        else:
            return render_template('upload.html', form=form)

    return app



if __name__ == "__main__":
    app = create_app()
    db = create_db()
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


