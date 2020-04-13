import os
import datetime
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Item, Category

ITEMS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Header
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/items', methods=['GET'])
    def get_items():
        all_items = Item.query.order_by(Item.id).all()
        current_items = paginate_items(request, all_items)

        if len(current_items) == 0:
            abort(204)
        else:
            return jsonify({
                'success': True,
                'items': current_items
            }), 200

    @app.route('/items', methods=['POST'])
    def create_item():
        body = request.get_json()
        description = body.get('description', None)
        amount = body.get('amount', 0)
        date = body.get('date', datetime.date.today)
        category_id = body.get('category_id', 1)

        try:
            item = Item(description=description, amount=amount, date=date, category_id=category_id)
            item.insert()

            selection = Item.query.order_by(Item.id).all()
            current_items = paginate_items(request, selection)

            return jsonify({
                'success': True,
                'created': item.id,
                'items': current_items
            }), 201

        except:
            abort(422)

    @app.route('/items/<int:item_id>', methods=['PATCH'])
    def edit_item(item_id):
        body = request.get_json()
        description = body.get('description', None)
        amount = body.get('amount', None)
        date = body.get('date', None)
        category_id = body.get('category_id', None)

        item = Item.query.get(item_id)
        if item:
            if description:
                item.description = description
            if amount:
                item.amount = amount
            if date:
                item.date = date
            if category_id:
                item.category_id = category_id
            item.update()
        else:
            new_item = Item(description=description, amount=amount, date=date, category_id=category_id)
            new_item.insert()
        
        return jsonify({
            'success': True
        }), 200

    @app.route('/items/<int:item_id>', methods=['DELETE'])
    def delete_item(item_id):
        item = Item.query.get(item_id)
        if item:
            item.delete()
            return jsonify({
                'success': True
            }), 200
        else:
            abort(404)

    @app.route('/categories/<id:category_id>/items', methods=['GET'])
    def get_items(category_id):
        category = Category.query.get(category)
        if category:
            items = Item.query.filter(Item.category_id==category_id).all()
            if len(items) == 0:
                return jsonify({
                    'sucess': True
                }), 204
            else:
                return jsonify({
                    'success': True,
                    'items': items,
                    'category_id': category_id
                }), 200
        else:
            abort(404)

    return app

def paginate_items(request, all_items):
    page = request.args.get('page', 1, type=int)
    start = (page-1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    items = [item.format() for item in all_items]
    return items[start:end]

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
