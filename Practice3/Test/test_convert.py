import unittest
from Practice3.Converter.convert import *


class ConvertTest(unittest.TestCase):
    def setUp(self):
        self.conv = Convert()

    def test_conversion(self):
        self.assertEqual(self.conv.convert_it(1, "Meter", "Centimeter"), 100)

    if __name__ == '__main__':
        unittest.main()
