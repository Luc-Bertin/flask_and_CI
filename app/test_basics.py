import os
import unittest

from flaskapp import app
from redis import Redis


class CounterTest(unittest.TestCase):
    ### step up and teardown ###
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass
    
    # actual tests #
    def test_welcome_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_redis_connection(self):
        redis = Redis(host="redis-server", db=0)
        self.app.get("/visit")
        self.assertEqual(int(redis.get("counter")), 1)


if __name__ == "__main__":
    unittest.main()
