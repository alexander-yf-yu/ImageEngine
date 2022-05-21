from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import os

from forms import ImageUploadForm
from models import Image, db

collection_name = os.environ['COLLECTION_NAME']
image_dir = os.environ['IMAGE_DIR']

def create_db():
    # using service account in environment
    # db = firestore.Client()
    db = firestore.Client.from_service_account_json("shopify-data-gcr-key.json")
    return db

def create_app():
    app = Flask(__name__)
    #app = Flask(__name__, static_url_path='', static_folder='/static')
    #app = Flask(__name__, static_url_path='')
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    Bootstrap(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        images = Image.query.all()
        return render_template('index.html', images=images)

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        form = ImageUploadForm()

        if form.validate_on_submit():
            f = form.image.data
            f_name = secure_filename(f.filename)
            img = form.image.data
            img.save(os.path.join(image_dir, secure_filename(f.filename)))

            new_record = Image(filename=f_name, description=form.description.data)
            db.session.add(new_record)
            db.session.commit()
            
            return redirect(url_for('hello_world'))
        else:
            return render_template('upload.html', form=form)

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


