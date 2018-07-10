from unittest import TestCase
from section6.models.store import StoreModel
from section6.models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        StoreModel('test').save_to_db()
        item = ItemModel('test', 19.99, 1)

        self.assertEqual(item.name, 'test',
                         "The name of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.price, 19.99,
                         "The price of the item after creation does not equal the constructor argument.")

    def test_item_json(self):
        item = ItemModel('test', 19.99,1)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(
            item.json(),
            expected,
            "The JSON export of the item is incorrect. Received {}, expected {}.".format(item.json(), expected))
