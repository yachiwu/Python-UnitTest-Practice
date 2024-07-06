import unittest
from src.Calculator import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_add(self):
        # arrange - prepare the need  for the test
        test_input = [
            (3, 5), 
            (-1, 1),  
            (-1, -1)  
        ]
        test_output = [8,0,-2]
        # act
        for i, params in enumerate(test_input):
            a, b = params
            expected = test_output[i]
            result = self.calc.add(a, b)
            # assert: 驗證結果是否符合預期
            self.assertEqual(result, expected) 

    def test_subtract(self):
        # arrange - prepare the need  for the test
        test_input = [
            (3, 5), 
            (-1, 1),  
            (-1, -1)  
        ]
        test_output = [-2,-2,0]
        # act
        for i, params in enumerate(test_input):
            a, b = params
            expected = test_output[i]
            result = self.calc.subtract(a, b)
            # assert: 驗證結果是否符合預期
            self.assertEqual(result, expected)        

if __name__ == "__main__":
    unittest.main()        