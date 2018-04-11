from unittest import TestCase
import numpy as np
import solutions

class EuropeanOption:
    strike = 1.0
    spot_price = 1.0
    time_to_maturity = 1.0
    volatility = 0.20
    zero_rate = 0.03
    dividends = 0.0
    

class EuropeanOptionMCTest(TestCase):
    
    def __init__(self, testname, student_function):
        super(EuropeanOptionMCTest, self).__init__(testname)
        self.student_function = student_function
    
    def test_call(self):
        option = EuropeanOption()
        discount_factor = np.exp(-option.zero_rate*option.time_to_maturity)
        forward = option.spot_price/discount_factor
        number_of_samples = 1000
        np.random.seed(218423)
        expected_price = solutions.EuropeanOptionMC(forward, option.strike, discount_factor, option.time_to_maturity, option.volatility, number_of_samples, 1)
        actual_price = self.student_function(forward, option.strike, discount_factor, option.time_to_maturity, option.volatility, number_of_samples, 1)
        self.assertEqual(expected_price, actual_price)
        