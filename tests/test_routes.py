import pytest
from flask import url_for
from flask_app import app

def test_hello_world():
    test_app = app.create_app()
    with test_app.test_client() as c:
        rs = c.get('/')
    assert rs.status_code == 200

def test_upload():
    test_app = app.create_app()
    with test_app.test_client() as c:
        rs = c.get('upload')
    assert rs.status_code == 200


