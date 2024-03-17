from flask import jsonify, request

from app import app, db
from app.models.order_model import Order
from app.schemas import OrderSchema


@app.route('/orders', methods=['POST'])
def create_order():
    try:
        user_id = request.json.get('user_id')
        course_id = request.json.get('course_id')
        level = request.json.get('level')

        new_order = Order(user_id=user_id, course_id=course_id, level=level)
        db.session.add(new_order)
        db.session.commit()

        return OrderSchema().jsonify(new_order), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/orders', methods=['GET'])
def get_orders():
    try:
        all_orders = Order.query.all()
        result = OrderSchema(many=True).dump(all_orders)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({'error': 'Order not found'}), 404
        return OrderSchema().jsonify(order), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({'error': 'Order not found'}), 404

        user_id = request.json.get('user_id')
        course_id = request.json.get('course_id')
        level = request.json.get('level')

        if user_id:
            order.user_id = user_id
        if course_id:
            order.course_id = course_id
        if level:
            order.level = level

        db.session.commit()
        return OrderSchema().jsonify(order), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    try:
        order = Order.query.get(order_id)
        if not order:
            return jsonify({'error': 'Order not found'}), 404

        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
