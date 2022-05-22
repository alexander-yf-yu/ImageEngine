from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import enum
from sqlalchemy import Enum
from datetime import datetime


db = SQLAlchemy()

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=True)
    pub_date = db.Column(db.Date, nullable=False, default=datetime.today)

    # tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
    # tag = db.relationship('Tag', backref=db.backref('images', lazy=True))

    def __repr__(self):
        return '<Image %r>' % self.filename


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Tag %r>' % self.name
