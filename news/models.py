from database import db

class NewsPost(db.Model):
    __tablename__ = 'news'
    #__table_args__ = { 'extend_existing': True }
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80))
    date = db.Column(db.Date)
    content = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',backref='news')
    live = db.Column(db.Boolean)

    def __init__(self, date, category):
        self.date = date
        self.category = category
        self.live = True

    def __repr__(self):
        return "<NewsPost> Title: %s, Date: %s, Content: %s, Category: %s" % (
                self.title,
                self.date,
                self.content,
                self.category
            )

class Category(db.Model):
    __tablename__ = 'category'
    #__table_args__ = { 'extend_existing': True }
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return "<Category> Name: %s" % (self.name)