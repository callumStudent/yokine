from yokine import app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

db = SQLAlchemy(app)

#Migrations
migrate = Migrate(app, db)