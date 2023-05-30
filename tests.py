import unittest
from fractions import Fraction
from unittest.mock import patch
import io
import main

from main import parse_fraction, perform_operation

class FractionCalculatorTestCase(unittest.TestCase):
    def test_parse_fraction_whole_number(self):
        result = parse_fraction("5")
        self.assertEqual(result, Fraction(5))
    
    def test_parse_fraction_proper_fraction(self):
        result = parse_fraction("3/4")
        self.assertEqual(result, Fraction(3, 4))
    
    def test_parse_fraction_mixed_number(self):
        result = parse_fraction("1&3/4")
        self.assertEqual(result, Fraction(7, 4))
    
    def test_perform_operation_multiply(self):
        result = perform_operation(Fraction(1, 2), "*", Fraction(3, 4))
        self.assertEqual(result, Fraction(3, 8))
    
    def test_perform_operation_divide(self):
        result = perform_operation(Fraction(2, 3), "/", Fraction(1, 4))
        self.assertEqual(result, Fraction(8, 3))
    
    def test_perform_operation_add(self):
        result = perform_operation(Fraction(2, 3), "+", Fraction(1, 4))
        self.assertEqual(result, Fraction(11, 12))
    
    def test_perform_operation_subtract(self):
        result = perform_operation(Fraction(3, 4), "-", Fraction(1, 2))
        self.assertEqual(result, Fraction(1, 4))
    
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_program_execution(self, mock_stdout):
        with patch("builtins.input", side_effect=["1/2 * 3/4", "exit"]):
            main.main()
        
        expected_output = "= 3/8\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
