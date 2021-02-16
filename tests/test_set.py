import unittest

from app import app, store


class TestSet(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        store.clear()

    def tearDown(self) -> None:
        store.clear()

    def test_can_write(self):
        res = self.client.post('SET/test_key/test_value')
        self.assertEqual(res.get_data(), b'OK')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(store.get('test_key'), 'test_value')
