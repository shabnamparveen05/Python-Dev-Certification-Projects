import unittest
from probability_calculator import Hat, experiment

class TestProbabilityCalculator(unittest.TestCase):

    def test_successful_experiment(self):
        hat = Hat(red=3, blue=2, green=1)
        result = experiment(hat, {'red': 1, 'blue': 1}, 2, 1000)
        self.assertGreater(result, 0.0, "The probability should be greater than 0")

    def test_no_successful_experiment(self):
        hat = Hat(red=2, blue=2)
        result = experiment(hat, {'red': 3}, 2, 1000)
        self.assertEqual(result, 0.0, "The probability should be 0 if the condition can't be met")

    def test_experiment_with_all_balls_drawn(self):
        hat = Hat(red=5, blue=5)
        result = experiment(hat, {'red': 5, 'blue': 5}, 10, 1000)
        self.assertGreater(result, 0.0, "The probability should be greater than 0")

    def test_edge_case_no_balls_drawn(self):
        hat = Hat(red=3, blue=2)
        result = experiment(hat, {'red': 0, 'blue': 0}, 0, 1000)
        self.assertEqual(result, 1.0, "The probability should be 1.0 if no balls are drawn")

if __name__ == '__main__':
    unittest.main()
