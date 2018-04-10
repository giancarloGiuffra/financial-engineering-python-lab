from unittest import TestCase

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
    
    def test_simple_function_that_adds_17(self):
        self.assertEqual(self.student_function(1), 18)
        self.assertEqual(self.student_function(10), 27)
        self.assertEqual(self.student_function(-6), 11)
    
    def test_call(self, student_function):
        pass
        