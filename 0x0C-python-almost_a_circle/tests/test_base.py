import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ A class to test the Base class. """

    def setUp(self):
        Base.__nb_objects = 0

    def TearDown(self):
        """ Adds code at the end of each instance. """
        pass

    def test_no_arg(self):
        """ Test with no arguments. """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_two_args(self):
        """ Passing two aruments. """
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_three_bases(self):
        """ Test with three args. """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)


if __name__ == "__main__":
    unittest.main()
