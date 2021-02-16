import unittest

from app import app, store


class TestKeys(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        store.clear()

    def tearDown(self) -> None:
        store.clear()

    def test_can_return(self):
        store['test_key'] = 'test_value'
        store['other_test_key'] = 'other_test_value'
        res = self.client.get('/KEYS/*')
        self.assertEqual(
            res.get_data(),
            b'1) "test_key"\n2) "other_test_key"\n',
        )
        self.assertEqual(res.status_code, 200)

    def test_no_keys(self):
        res = self.client.get('/KEYS/*')
        self.assertEqual(res.get_data(), b'')
        self.assertEqual(res.status_code, 404)
