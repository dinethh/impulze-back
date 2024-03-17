from flask_marshmallow import Marshmallow

ma = Marshmallow()


class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'name', 'email', 'contact', 'password')


class CourseSchema(ma.Schema):
    class Meta:
        fields = ('course_id', 'image_url', 'title')


class OrderSchema(ma.Schema):
    user = ma.Nested(UserSchema)
    course = ma.Nested(CourseSchema)

    class Meta:
        fields = ('order_id', 'user', 'course', 'level')
