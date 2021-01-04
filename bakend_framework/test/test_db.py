# from backend import db
from bakend_framework.src.backend import db


def test_create_table():
    db.create_all()