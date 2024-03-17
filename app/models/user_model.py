from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contact = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    # One-to-Many with Order
    orders = db.relationship('Order', backref='user', lazy=True)
