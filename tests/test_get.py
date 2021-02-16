import unittest

from app import app, store


class TestGet(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        store.clear()

    def tearDown(self) -> None:
        store.clear()

    def test_can_return(self):
        store['test_key'] = 'test_value'
        res = self.client.get('/GET/test_key')
        self.assertEqual(res.get_data(), b'test_value')
        self.assertEqual(res.status_code, 200)

    def test_key_doesnt_exist(self):
        res = self.client.get('/GET/not_existing_key')
        self.assertEqual(res.get_data(), b"Key doesn't exist.")
        self.assertEqual(res.status_code, 404)
