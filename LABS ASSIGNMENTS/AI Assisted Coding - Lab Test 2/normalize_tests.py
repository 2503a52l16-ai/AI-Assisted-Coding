import unittest
from normalize_solution import normalize

class TestNormalize(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(normalize([10, 20, 30]), [0.0, 0.5, 1.0])

    def test_empty_list(self):
        self.assertEqual(normalize([]), [])

    def test_all_equal(self):
        self.assertEqual(normalize([5, 5, 5]), [0.0, 0.0, 0.0])

    def test_single_value(self):
        self.assertEqual(normalize([42]), [0.0])

    def test_negative_values(self):
        self.assertEqual(normalize([-5, 0, 5]), [0.0, 0.5, 1.0])

if __name__ == "__main__":
    unittest.main()
