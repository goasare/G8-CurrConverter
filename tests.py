import unittest
from app import convert_curr 

class TestConverter(unittest.TestCase):

    def test_usd_to_ghs(self):
        result = convert_curr(1, "USD", "GHS")
        self.assertGreater(result, 0) 

    # def test_same_currency(self):
    #     result = convert_curr(100, "USD", "USD")
    #     self.assertEqual(result, 100)   

    #     def test_ghs_to_usd(self):
    #     result = convert_curr(100, "GHS", "USD")
    #     self.assertGreater(result, 0)

    # def test_ghs_to_gbp(self):
    #     result = convert_curr(100, "GHS", "GBP")
    #     self.assertGreater(result, 0)

    # def test_ghs_to_eur(self):
    #     result = convert_curr(100, "GHS", "EUR")
    #     self.assertGreater(result, 0)

    # def test_ghs_to_jpy(self):
    #     result = convert_curr(100, "GHS", "JPY")
    #     self.assertGreater(result, 0)

if __name__ == '__main__':
    unittest.main()