import unittest
import kudos.views as kudos


class IntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = kudos.app.test_client()

    def test_example_end_point(self):
        result = self.app.get("/")
        self.assertEqual(result.data, bytes("Hello World!", "utf8"))
