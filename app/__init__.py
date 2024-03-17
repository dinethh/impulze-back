from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

from app.models import user_model, course_model,order_model
from app.routes import user_route, course_route,order_routes

with app.app_context():
    db.create_all()
