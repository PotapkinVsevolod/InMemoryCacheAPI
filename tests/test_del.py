import unittest

from app import app, store


class TestDel(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        store.clear()

    def tearDown(self) -> None:
        store.clear()

    def test_can_delete(self):
        store['test_key'] = 'test_value'
        res = self.client.delete('/DEL/test_key')
        self.assertEqual(res.status_code, 204)
        self.assertIsNone(store.get('test', None))

    def test_key_doesnt_exist(self):
        res = self.client.delete('/DEL/not_existing_key')
        self.assertEqual(res.get_data(), b"Key doesn't exist.")
        self.assertEqual(res.status_code, 404)
