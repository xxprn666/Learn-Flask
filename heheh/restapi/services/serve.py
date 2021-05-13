from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from services.config import Development

app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
Migrate(app,db)

