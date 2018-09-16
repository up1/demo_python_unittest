import unittest
from calculator import add
 
class CalculatorTest(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numbers_3_4(self):
        self.assertEqual( add(3, 4), 7)
 
    def test_strings_5_3(self):
        self.assertEqual( add(5, 3), 8)
    
    def test_strings_5_4(self):
        self.assertEqual( add(5,4), 9)
 
if __name__ == '__main__':
    unittest.main()