import pytest
from flask import url_for
from flask_app import app

def test_connect_db_connection():
    db = app.create_db()
    assert 'shopify' in db.project

