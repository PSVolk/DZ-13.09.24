class NumberSet:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def average(self):
        return sum(self.numbers) / len(self.numbers)

    def max(self):
        return max(self.numbers)

    def min(self):
        return min(self.numbers)

import unittest

class TestNumberSet(unittest.TestCase):
    def test_sum(self):
        number_set = NumberSet([1, 2, 3, 4, 5])
        self.assertEqual(number_set.sum(), 15)

    def test_average(self):
        number_set = NumberSet([1, 2, 3, 4, 5])
        self.assertEqual(number_set.average(), 3)

    def test_max(self):
        number_set = NumberSet([1, 2, 3, 4, 5])
        self.assertEqual(number_set.max(), 5)

    def test_min(self):
        number_set = NumberSet([1, 2, 3, 4, 5])
        self.assertEqual(number_set.min(), 1)

    def test_empty_set(self):
        number_set = NumberSet([])
        self.assertEqual(number_set.sum(), 0)
        self.assertEqual(number_set.average(), 0)
        with self.assertRaises(ValueError):
            number_set.max()
        with self.assertRaises(ValueError):
            number_set.min()

if __name__ == '__main__':
    unittest.main()
