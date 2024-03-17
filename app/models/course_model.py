from app import db


class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(100), nullable=False)

    # One-to-Many with Order
    orders = db.relationship('Order', backref='course', lazy=True)
