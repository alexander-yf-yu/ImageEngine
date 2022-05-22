from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import os

from forms import ImageUploadForm, ImageSearchForm
from models import Image, db

IMAGE_DIR = os.environ['IMAGE_DIR']

def create_app():
    app = Flask(__name__)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    Bootstrap(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route("/")
    def index(images=None):
        if not images:
            images = Image.query.all()
        return render_template('index.html', images=images)

    @app.route("/search", methods=['GET', 'POST'])
    def search():
        form = ImageSearchForm()

        if form.validate_on_submit():
            search_text = '%{0}%'.format(form.text.data)
            print(search_text)
            print(type(search_text))
            if search_text:
                # filtered = Image.query.filter(Image.description.contains(search_text))
                filtered = Image.query.filter(Image.description.ilike(search_text))
                print(filtered)
                return redirect(url_for('index', images=filtered))
            else:
                return redirect(url_for('index'))
        else:
            return render_template('search.html', form=form)

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        form = ImageUploadForm()

        if form.validate_on_submit():
            f = form.image.data
            f_name = secure_filename(f.filename)
            img = form.image.data
            img.save(os.path.join(IMAGE_DIR, secure_filename(f.filename)))

            new_record = Image(filename=f_name, description=form.description.data)
            db.session.add(new_record)
            db.session.commit()

            images = Image.query.all()

            return redirect(url_for('index'))
        else:
            return render_template('upload.html', form=form)

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


