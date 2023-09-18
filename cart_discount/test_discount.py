import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    # def test_list_of_less_than_three_prices(self):
    #     self.assertEqual(None,discount([10, 4]))

    # def test_list_of_less_with_one_price(self):
    #     self.assertEqual(10, discount([10, 10, 10,]))

    # def test_list_of_two_prices_no_discount(self):
    #     prices = [20, 1]#arrange
    #     expexted_discount = 0#arrange
    #     actual_discount = discount(prices)#action
    #     self.assertEqual(expexted_discount, actual_discount)#assert

    
    # def test_list_of_less_than_three_items(self.)
    #     self.fail('test')
    
    # def test_list


    # def test_rturnswhencalledwith1item(self):
    #     self.fail('Finish this test')
    # # TODO more unit tests here. Each test should test one scenario
    # #what if function is called isnt a list or a weird data type?

if __name__ == '__main__':
    unittest.main()