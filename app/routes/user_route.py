from random import randint

from flask import jsonify, request
from flask_mail import Mail, Message

from app import app, db
from app.models.user_model import User
from app.schemas import UserSchema

mail = Mail(app)


def send_otp_email(recipient, otp):
    subject = "Your One-Time Password (OTP)"
    body = f"Your OTP is: {otp}"
    msg = Message(subject, recipients=[recipient])
    msg.body = body
    mail.send(msg)


@app.route('/register', methods=['POST'])
def create_user():
    try:
        name = request.json.get('name')
        email = request.json.get('email')
        contact = request.json.get('contact')
        password = request.json.get('password')

        otp = str(randint(100000, 999999))

        new_user = User(name=name, email=email, contact=contact, password=password)
        db.session.add(new_user)
        db.session.commit()

        send_otp_email(email, otp)

        return UserSchema().jsonify(new_user), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return "Welcome!"
        else:
            return "Invalid email or password"
    except Exception as e:
        return str(e)


@app.route('/users', methods=['GET'])
def get_users():
    try:
        all_users = User.query.all()
        result = UserSchema(many=True).dump(all_users)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
