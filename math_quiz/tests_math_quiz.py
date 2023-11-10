import unittest
from math_quiz import generate_random_integer, generate_operator, calculate_result

class TestMathFunctions(unittest.TestCase):
    def test_generate_random_integer_within_range(self):
        min_val = 1
        max_val = 10
        for _ in range(1000):
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_operator(self):
        # Test if operator generated is one of the valid arithmetic operators
        valid_operators = ['+', '-', '*']
        operator = generate_operator()
        self.assertIn(operator, valid_operators)

    def test_calculate_result(self):
        # Test cases for calculate_result function
        # Define some test cases to check if the calculations are correct
        test_cases = [
            (5, 2, '+', '5 + 2', 7),  # Example test case
            # Add more test cases as necessary
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_result(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == '__main__':
    unittest.main()
