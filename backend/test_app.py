import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import datetime

from app import create_app
from models import db, setup_db, Item, Category
from config import bearer_token

analyser_header = {"Authorization": bearer_token['analyser']}
data_owner_header = {"Authorization": bearer_token['data_owner']}


def add_one_item():
    item = Item(description='Bread', category_id=1, amount=8.5,
                date=datetime.date(2020, 3, 14), expense=True)
    item.insert()


class FizTestCase(unittest.TestCase):
    valid_item = {
        "description": "florist",
        "amount": "8.99",
        "date": "20200308",
        "expense": True,
        "category_id": 4
    }
    invalid_item = {
        "description": "Tax return",
        "date": "20200310",
        "expense": False,
        "category_id": 3
    }
    patch_item = {
        "amount": "9.88"
    }

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "fiz_test"
        self.database_path = "postgresql://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        db.drop_all()
        db.create_all()
        db.engine.execute(
            "INSERT INTO categories (id, type) VALUES (1, 'Food');")
        db.engine.execute(
            "INSERT INTO categories (id, type) VALUES (2, 'Housing');")
        db.engine.execute(
            "INSERT INTO categories (id, type) VALUES (3, 'Salary');")
        db.engine.execute(
            "INSERT INTO categories (id, type) VALUES (4, 'Leisure');")
        db.engine.execute('commit;')

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def test_get_zero_items(self):
        res = self.client().get('/items', headers=data_owner_header)
        self.assertEqual(res.status_code, 204)

    def test_get_one_item(self):
        add_one_item()
        res = self.client().get('/items', headers=data_owner_header)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(len(data['items']) == 1)

    def test_post_valid_item(self):
        res = self.client().post('/items', json=self.valid_item, headers=data_owner_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertTrue(data['created'])

    def test_post_invalid_item(self):
        res = self.client().post('/items', json=self.invalid_item, headers=data_owner_header)
        self.assertEqual(res.status_code, 422)

    def test_delete_valid_item(self):
        add_one_item()
        res = self.client().delete('/items/1', headers=data_owner_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['deleted'])

    def test_delete_invalid_item(self):
        res = self.client().delete('/items/1', headers=data_owner_header)
        self.assertEqual(res.status_code, 404)

    def test_patch_item(self):
        add_one_item()
        res = self.client().patch('/items/1', json=self.patch_item, headers=data_owner_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_patch_invalid_item(self):
        res = self.client().patch('/items/1', json=self.patch_item, headers=data_owner_header)
        self.assertEqual(res.status_code, 404)

    def test_get_items_by_category(self):
        add_one_item()
        res = self.client().get('/categories/1/items', headers=data_owner_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data['items']), 1)

    def test_get_items_by_empty_category(self):
        res = self.client().get('/categories/1/items', headers=data_owner_header)
        self.assertEqual(res.status_code, 204)

    def test_get_items_by_invalid_category(self):
        res = self.client().get('/categories/10/items', headers=data_owner_header)
        self.assertEqual(res.status_code, 404)

    def test_delete_items_by_analyser(self):
        res = self.client().delete('/items/1', headers=analyser_header)
        self.assertEqual(res.status_code, 403)

    def test_delete_without_authorization(self):
        res = self.client().delete("/items/1")
        self.assertEqual(res.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
