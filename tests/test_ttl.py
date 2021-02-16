import time
import unittest

from app import app, store, ttl


class TestTTL(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        store.clear()
        ttl.clear()

    def tearDown(self) -> None:
        store.clear()
        ttl.clear()

    def test_can_set_ttl_in_seconds(self):
        self.client.post('SET/test_key/test_value/EX=5')
        self.assertIn('test_key', ttl)
        self.assertIn('test_key', store)
        time.sleep(5)
        self.client.get('GET/something_key')
        self.assertNotIn('test_key', ttl)
        self.assertNotIn('test_key', store)

    def test_can_set_ttl_in_milliseconds(self):
        self.client.post('SET/test_key/test_value/PX=100')
        self.assertIn('test_key', ttl)
        self.assertIn('test_key', store)
        time.sleep(0.1)
        self.client.get('GET/something_key')
        self.assertNotIn('test_key', ttl)
        self.assertNotIn('test_key', store)

    def test_can_set_ttl_in_seconds_and_milliseconds(self):
        self.client.post('SET/test_key/test_value/EX=1/PX=100')
        self.assertIn('test_key', ttl)
        self.assertIn('test_key', store)
        time.sleep(1.1)
        self.client.get('GET/something_key')
        self.assertNotIn('test_key', ttl)
        self.assertNotIn('test_key', store)

    def test_can_set_ttl_in_milliseconds_and_seconds(self):
        self.client.post('SET/test_key/test_value/PX=100/EX=1')
        self.assertIn('test_key', ttl)
        self.assertIn('test_key', store)
        time.sleep(1.1)
        self.client.get('GET/something_key')
        self.assertNotIn('test_key', ttl)
        self.assertNotIn('test_key', store)

    def test_reset_key(self):
        self.client.post('SET/test_key/test_value/EX=1')
        self.client.post('SET/test_key/test_value/EX=3')
        time.sleep(1)
        self.client.get('GET/something_key')
        self.assertEqual(len(ttl), 1)
        self.assertIn('test_key', ttl)
        self.assertIn('test_key', store)
