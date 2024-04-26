import unittest
from io import StringIO
import sys
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ A class to test the Square class. """

    def SetUp(self):
        pass

    def TearDown(self):
        pass

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Rectangle)

    def test_no_args(self):
        """ Test no arguments. """
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """ Test one argument. """
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        """ Test two arguments. """
        s1 = Square(10, 2)
        s2 = Square(11, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_str(self):
        """ Test the str method. """
        squ = Square(10, 1, 1, 7)
        captured_output = StringIO()
        expected_output = "[Square] (7) 1/1 - 10"

        with redirect_stdout(captured_output):
            print(squ)

        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_new_square(self):
        """ Testing new square. """
        square = Square(2)
        self.assertEqual(square.width, 2)

    def test_not_int(self):
        """ Testing with size not an int. """
        with self.assertRaises(TypeError):
            Square([])
            Square({})
            Square({2})
            Square({2, 5})
            Square(0.5)
            Square(True)
            Square(False)
            Square("Hello")

    def test_size_zero(self):
        """ Testing size with zero value. """
        with self.assertRaises(ValueError):
            Square(0)

    def test_negative_size(self):
        """ Testing with a negative value. """
        with self.assertRaises(ValueError):
            Square(-1)

    def test_all_args(self):
        """ Passing all args. """
        s1 = Square(1, 0, 0)
        s2 = Square(3, 2, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s2.height, 3)
        self.assertEqual(s2.width, 3)


if __name__ == "__main__":
    unittest.main()
