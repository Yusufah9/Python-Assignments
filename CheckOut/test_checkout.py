import unittest
from checkout import calculate_sub_total, calculate_discount, calculate_vat, calculate_bill_total, calculate_balance


class TestCheckOut(unittest.TestCase):

    def test_calculate_sub_total(self):
        prices = [2100.0, 550.0]
        quantities = [2, 2]
        self.assertEqual(calculate_sub_total(prices, quantities), 5300.0)

    def test_calculate_discount(self):
        prices = [2100.0, 550.0]
        quantities = [2, 2]
        self.assertEqual(calculate_discount(prices, quantities, 8.0), 424.0)

    def test_calculate_vat(self):
        prices = [2100.0, 550.0]
        quantities = [2, 2]
        self.assertEqual(calculate_vat(prices, quantities), 927.5)

    def test_calculate_bill_total(self):
        prices = [2100.0, 550.0]
        quantities = [2, 2]
        self.assertEqual(calculate_bill_total(prices, quantities, 8.0), 5803.5)

    def test_calculate_balance(self):
        bill_total = 5803.5
        amount_paid = 6000.0
        self.assertEqual(calculate_balance(bill_total, amount_paid), 196.5)
