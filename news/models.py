from yokine import db
from datetime import datetime

Class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    date = db.Column(db.DateTime)
    content = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('news', lazy='dynamic'))
    live = db.Column(db.Boolean)

    def __init__(self):
        self.live = True

Class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))