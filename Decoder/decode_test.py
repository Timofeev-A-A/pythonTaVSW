import unittest
from decoder import Decoder


class DecodeTest(unittest.TestCase):
    def setUp(self):
        self.deco = Decoder()

    def test_decoder1(self):
        self.assertEqual(self.deco.decode([18, 10, 10, 31, 8, 20, 5, 36, 13, 14, 22, 12], 9754761), "ice and fire")

    def test_decoder2(self):
        self.assertEqual(self.deco.decode([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939), "masterpiece")

    def test_coder1(self):
        self.assertEqual(self.deco.coder("microsoft", 7463), [20, 13, 9, 21, 22, 23, 21, 9, 27])

    def test_coder2(self):
        self.assertEqual(self.deco.coder("container", 46532), [7, 21, 19, 23, 3, 13, 20, 10, 21])


if __name__ == '__main__':
    unittest.main()
