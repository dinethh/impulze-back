from flask import jsonify, request

from app import app, db
from app.models.course_model import Course
from app.schemas import CourseSchema


@app.route('/courses', methods=['POST'])
def create_course():
    try:

        image_url = request.json.get('image_url')
        title = request.json.get('title')

        new_course = Course(title=title, image_url=image_url)
        db.session.add(new_course)
        db.session.commit()

        return CourseSchema().jsonify(new_course), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        all_courses = Course.query.all()
        result = CourseSchema(many=True).dump(all_courses)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    try:
        course = Course.query.get(course_id)
        if not course:
            return jsonify({'error': 'Course not found'}), 404
        return CourseSchema().jsonify(course), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    try:
        course = Course.query.get(course_id)
        if not course:
            return jsonify({'error': 'Course not found'}), 404

        title = request.json.get('title')
        image_url = request.json.get('image_url')

        if title:
            course.title = title
        if image_url:
            course.image_url = image_url

        db.session.commit()
        return CourseSchema().jsonify(course), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    try:
        course = Course.query.get(course_id)
        if not course:
            return jsonify({'error': 'Course not found'}), 404

        db.session.delete(course)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
