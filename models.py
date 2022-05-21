from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import enum
from sqlalchemy import Enum

class Tag(enum.Enum):
    art = "art"
    people = "people"
    nature = "nature"
    tech = "tech"
    misc = "misc"

db = SQLAlchemy()

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=True)
    # tag = db.Column(db.Enum(('art', 'people', 'nature', 'tech', 'misc')))

    def __repr__(self):
        return '<Image %r>' % self.filename
