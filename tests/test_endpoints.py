# tests/test_basic.py
import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that Flask was set up correctly
    def test_account(self):
        tester = app(self)
        response = tester.get('/account')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
