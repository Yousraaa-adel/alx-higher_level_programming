import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ Test new Rectangle class. """
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle2(self):
        """ Test a new Rectangle with all the arguments. """
        new = Rectangle(3, 4, 1, 1, 7)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 4)
        self.assertEqual(new.x, 1)
        self.assertEqual(new.y, 1)
        self.assertEqual(new.id, 7)

    def test_zero_width(self):
        """ Test a zero width value."""
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_negative_width(self):
        """ Test a negative width value."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
            Rectangle(-9, 1)

            Rectangle(-1, -1)

    def test_negative_height(self):
        """ Test a negative height value."""
        with self.assertRaises(ValueError):
            Rectangle(8, -1)
            Rectangle(1, -3)

    def test_negative_x(self):
        """ Test a negative x value. """
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
            Rectangle(1, 1, 0)

    def test_negative_y(self):
        """ Test a negative y value. """
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -5)
            Rectangle(1, 1, -1, -5)
            Rectangle(1, 1, -1, 0)

    def test_non_int_width(self):
        """ Test non-int width values. """
        with self.assertRaises(TypeError):
            Rectangle(0.5, 2)
            Rectangle({}, 2)
            Rectangle([], 2)
            Rectangle([1], 2)
            Rectangle({1}, 2)

            Rectangle({}, [])

    def test_non_int_height(self):
        """ Test non-int height values. """
        with self.assertRaises(TypeError):
            Rectangle(2, 0.5)
            Rectangle(2, {})
            Rectangle(2, [])
            Rectangle(2, [1])
            Rectangle(2, {1})

    def test_non_int_x(self):
        """ Test non-int x values. """
        with self.assertRaises(TypeError):
            Rectangle(2, 1, 0.5, 4)
            Rectangle(2, 4, {}, 8)
            Rectangle(2, 3, [], 3)
            Rectangle(2, 1, [1], 3)
            Rectangle(2, 2, {1}, 3)

    def test_non_int_y(self):
        """ Test non-int y values. """
        with self.assertRaises(TypeError):
            Rectangle(2, 1, 4, 0.5)
            Rectangle(2, 4, 2, {})
            Rectangle(2, 3, 1, {})
            Rectangle(2, 1, 6, {1})
            Rectangle(2, 2, 8, [1])
            Rectangle(2, 2, {3}, [1])

    def test_area(self):
        """ Test calculating the area of the rectangle. """
        new = Rectangle(3, 2, 3, 4)
        self.assertEqual(6, 6)

    def test_display(self):
        """ Test displaying a new rectangle. """
        new = Rectangle(4, 6)
        captured_output = StringIO()
        sys.stdout = captured_output

        new.display()
        sys.stdout = sys.__stdout__

        expected_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()