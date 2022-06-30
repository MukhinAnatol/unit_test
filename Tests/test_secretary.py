import unittest
from unit_test.secretary import *


class Test_Class(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp method")

    def tearDown(self) -> None:
        print("tearDown method")

    def test_find_person(self):
      doc = "2207 876234"
      self.assertIsInstance(find_person(doc), str)

    def test_find_shelf(self):
        self.assertIsInstance(find_shelf('10006'), str)

    def test_make_list(self):
        self.assertIsInstance(make_list(), list)

    def test_add_doc(self):
        self.assertIsInstance(add_doc('passport', '531', 'Smith', '2'), dict)

    def test_del_doc(self):
        self.assertIsInstance(del_doc('11-2'), bool)

    def test_add_shelf(self):
        self.assertIsInstance(add_shelf('4'), bool)


    def test_move_doc(self):
        self.assertIsInstance(move_doc('11-2', '2'), str)