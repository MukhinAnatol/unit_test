import unittest
from unit_test.create_folder import YaUploader

fixture = [201, 400, 401, 404, 451, 498, 502, 503, 507]

class Test_Class(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp method")

    def tearDown(self) -> None:
        print("tearDown method")

    def test_create_folder(self):
        ya_disc_token = "string"
        ya = YaUploader(ya_disc_token)
        self.assertIn(ya.create_folder('new_folder'), fixture)

