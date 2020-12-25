import unittest
from client3 import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
 for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))



  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  """ ------------ Add more unit tests ------------ """

  def test_getRatio_priceBZero(self):
    price_a = 115.6
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))
 
  def test_getRatio_priceAZero(self):
    price_a = 0
    price_b = 112.4
    self.assertEqual(getRatio(price_a, price_b), 0)
 
  def test_getRatio_greaterThan1(self):
    price_a = 350.68
    price_b = 150.22
    self.assertGreater(getRatio(price_a, price_b), 1)

  def test_getRatio_LessThan1(self):
    price_a = 150.22
    price_b = 350.68
    self.assertLess(getRatio(price_a, price_b), 1)

  def test_getRatio_exactlyOne(self):
    price_a = 300.24
    price_b = 300.24
    self.assertEqual(getRatio(price_a, price_b), 1)


if __name__ == '__main__':
    unittest.main()
