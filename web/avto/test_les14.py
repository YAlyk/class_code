import unittest
import les14 as main
import statistics


class is_factorTests(unittest.TestCase):
    def test_isfactor(self):
        self.assertTrue(main.is_factor(3, 12))

    def test_isfactor(self):
        self.assertFalse(main.is_factor(5, 12))

    def test_isfactor(self):
        self.assertTrue(main.is_factor(7, 14))

    def test_isfactor(self):
        self.assertTrue(main.is_factor(2, 12))

    def test_isfactor(self):
        self.assertFalse(main.is_factor(7, 15))


if __name__ == '__main__':
    unittest.main()
