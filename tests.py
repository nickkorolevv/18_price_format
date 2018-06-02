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
        with self.assertRaises(ValueError):
            format_price("price")

    def test_incorrect_type(self):
        with self.assertRaises(TypeError):
            format_price(["123456789"])

    def test_float_with_comma(self):
        self.assertEqual(format_price("1111,1111"), "1 111.11")

    def test_float_with_zeros(self):
        self.assertEqual(format_price("12345.00"), "12 345")

    def test_dict_incorrect(self):
        with self.assertRaises(AttributeError):
            format_price({"1": 2, "2": 3})

    def test_incorrect_punctuation(self):
        with self.assertRaises(ValueError):
            format_price("!@#$%^&*()")



if __name__ == "__main__":
    unittest.main()
