import unittest
from Practice3.Converter.convert import *


class ConvertTest(unittest.TestCase):
    def setUp(self):
        self.conv = Convert()

    def test_length_conversion(self):
        self.assertEqual(self.conv.convert_it(1, 'length', 'm', 'cm'), 100)

    def test_square_conversion(self):
        self.assertEqual(self.conv.convert_it(3, 'square', 'sotka', 'sq. m'), 300)

    def test_volume_conversion(self):
        self.assertEqual(self.conv.convert_it(5, 'volume', 'ml', 'c. cm'), 5)

    def test_mass_conversion(self):
        self.assertEqual(self.conv.convert_it(16, 'mass', 'centner', 'ton'), 1.6)


if __name__ == '__main__':
    unittest.main()
