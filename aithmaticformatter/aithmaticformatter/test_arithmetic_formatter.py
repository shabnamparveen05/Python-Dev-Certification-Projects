import unittest
from arithmetic_formatter import arithmetic_arranger

class TestArithmeticFormatter(unittest.TestCase):

    def test_arrangement(self):
        result = arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49'])
        expected = '   32      3801      45      123\n+ 698    -    2    + 43    +  49\n-----    ------    ----    -----'
        self.assertEqual(result, expected)

    def test_too_many_problems(self):
        result = arithmetic_arranger(['32 + 698', '3801 - 2', '45 + 43', '123 + 49', '1 + 2', '1 + 1'])
        expected = 'Error: Too many problems.'
        self.assertEqual(result, expected)

    def test_operator_error(self):
        result = arithmetic_arranger(['32 * 698'])
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(result, expected)

    def test_non_digit_error(self):
        result = arithmetic_arranger(['32 + a698'])
        expected = 'Error: Numbers must only contain digits.'
        self.assertEqual(result, expected)

    def test_number_length_error(self):
        result = arithmetic_arranger(['12345 + 698'])
        expected = 'Error: Numbers cannot be more than four digits.'
        self.assertEqual(result, expected)

    def test_show_answers(self):
        result = arithmetic_arranger(['32 + 8', '1 - 3801', '9999 + 9999', '523 - 49'], True)
        expected = '   32         1      9999      523\n+  8    - 3801    + 9999    -  49\n----    ------    ------    ----\n  40     -3800     19998      474'
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
