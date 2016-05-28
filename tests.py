import unittest
import itertools
import json

import app

class FibonacciTest(unittest.TestCase):
    def test_fibonacci_function(self):
        gen = app.fibonacci()
        self.assertEqual(
            list(itertools.islice(gen, 0, 10)),
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        )

class ServiceTest(unittest.TestCase):
    def setUp(self):
        self.client = app.app.test_client()

    def test_successful_response(self):
        resp = self.client.get('/sequence/5')
        self.assertEqual(json.loads(resp.data), dict(sequence=[0, 1, 1, 2, 3]))

    def test_negative_number(self):
        resp = self.client.get('/sequence/-1')

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(json.loads(resp.data),
                         dict(error='N must not be less than 0'))

    def test_not_a_numbet(self):
        resp = self.client.get('/sequence/aaa')

        self.assertEqual(resp.status_code, 400)
        self.assertEqual(json.loads(resp.data),
                         dict(error='N must be a non-negative integer'))

    def test_empty_result(self):
        resp = self.client.get('/sequence/0')

        self.assertEqual(json.loads(resp.data), dict(sequence=[]))


if __name__ == '__main__':
    unittest.main()
