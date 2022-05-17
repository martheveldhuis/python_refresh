import unittest
import sum

class TestSumTwo(unittest.TestCase):
    
    def test_two_ints(self):
        a = 1
        b = 2
        result = sum.sum_two(a, b)
        self.assertEqual(result, 3)
        
if __name__ == '__main__':
    unittest.main()
