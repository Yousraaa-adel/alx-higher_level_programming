import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        Base.__nb_objects = 0
    
    def test_id(self):
        
    

        


if __name__ == "__main__":
    unittest.main()
