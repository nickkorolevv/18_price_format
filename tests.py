import unittest
from format_price import format_price


class PriceFormatTest(unittest.TestCase):
    def test_int_value(self):
        self.assertEqual(format_price(123456678), "123 456 678")

    def test_float_value(self):
        self.assertEqual(format_price(1123.45345), "1 123.45")

    def test_int_string(self):
        self.assertEqual(format_price("19231985439"), "19 231 985 439")

    def test_float_string(self):
        self.assertEqual(format_price("12345.6712"), "12 345.67")

    def test_incorrect_str(self):
        self.assertEqual(format_price("price"), None)

    def test_with_comma(self):
        self.assertEqual(format_price(["111,111"]), None)

    def test_incorrect_type(self):
        self.assertEqual(format_price(["123456789"]), None)

    def test_float_with_zeros(self):
        self.assertEqual(format_price("12345.00"), "12 345")

    def test_dict_incorrect(self):
        self.assertEqual(format_price({"1": 2, "2": 3}), None)

    def test_incorrect_punctuation(self):
        self.assertEqual(format_price("!@#$%^&*()"), None)

    def test_boolean(self):
        self.assertEqual(format_price(True), None)


if __name__ == "__main__":
    unittest.main()
