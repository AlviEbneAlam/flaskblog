
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY']='3307a18953ac6dc026371cf4afae108a'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db= SQLAlchemy(app)

from flaskblog import routes
