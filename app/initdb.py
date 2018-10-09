__author__ = 'houhuihua'
import db


def initDb():
    db.drop_tables()
    db.create_tables()


initDb()
