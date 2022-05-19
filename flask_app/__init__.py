from flask import Flask, request, redirect, url_for, render_template

def get_app():
    app = Flask(__name__)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    Bootstrap(app)
    return app


def get_db():
    db = firestore.Client()
    return db
