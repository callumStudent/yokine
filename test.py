import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from news.models import Category

news = Category.query.all()
for n in news:
    print n.title