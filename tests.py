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
        np.random.seed(218423)
        actual_price = self.student_function(forward, option.strike, discount_factor, option.time_to_maturity, option.volatility, number_of_samples, 1)
        self.assertAlmostEqual(expected_price, actual_price)
        
    def test_put(self):
        option = EuropeanOption()
        discount_factor = np.exp(-option.zero_rate*option.time_to_maturity)
        forward = option.spot_price/discount_factor
        number_of_samples = 1000
        np.random.seed(218423)
        expected_price = solutions.EuropeanOptionMC(forward, option.strike, discount_factor, option.time_to_maturity, option.volatility, number_of_samples, -1)
        np.random.seed(218423)
        actual_price = self.student_function(forward, option.strike, discount_factor, option.time_to_maturity, option.volatility, number_of_samples, -1)
        self.assertAlmostEqual(expected_price, actual_price)
        

class ReadSwapRatesTest(TestCase):

    file = 'MktData_CurveBootstrap.xls'
    sheet = 'Data'
    fromRow = 37
    numberOfRows = 50
    columnRange = 'D:F'
    
    def __init__(self, testname, student_function):
        super(ReadSwapRatesTest, self).__init__(testname)
        self.student_function = student_function
        self.expected_data_frame = solutions.ReadSwapRates(self.file, self.sheet, self.fromRow, self.numberOfRows, self.columnRange)

    def test_header(self):
        actual_data_frame = self.student_function(self.file, self.sheet, self.fromRow, self.numberOfRows, self.columnRange)
        self.assertEqual(self.expected_data_frame.columns.tolist(), actual_data_frame.columns.tolist())

    def test_number_of_rows(self):
        actual_data_frame = self.student_function(self.file, self.sheet, self.fromRow, self.numberOfRows, self.columnRange)
        self.assertEqual(self.expected_data_frame.shape[0], actual_data_frame.shape[0])

    def test_dates(self):
        actual_data_frame = self.student_function(self.file, self.sheet, self.fromRow, self.numberOfRows, self.columnRange)
        self.assertEqual(self.expected_data_frame.axes[0].tolist(), actual_data_frame.axes[0].tolist())

    def test_bids(self):
        actual_data_frame = self.student_function(self.file, self.sheet, self.fromRow, self.numberOfRows, self.columnRange)
        self.assertEqual(self.expected_data_frame.ix[:,0].tolist(), actual_data_frame.ix[:,0].tolist())

    def test_asks(self):
        actual_data_frame = self.student_function(self.file, self.sheet, self.fromRow, self.numberOfRows, self.columnRange)
        self.assertEqual(self.expected_data_frame.ix[:,1].tolist(), actual_data_frame.ix[:,1].tolist())


class ExtractDatesAndMidRatesTest(TestCase):

    file = 'MktData_CurveBootstrap.xls'
    sheet = 'Data'
    fromRow = 37
    numberOfRows = 50
    columnRange = 'D:F'
    
    def __init__(self, testname, student_function):
        super(ExtractDatesAndMidRatesTest, self).__init__(testname)
        self.student_function = student_function
        self.swap_rates = solutions.ReadSwapRates(self.file, self.sheet, self.fromRow, self.numberOfRows, self.columnRange)
        self.expected_dates, self.expected_mid_rates = solutions.ExtractDatesAndMidRates(self.swap_rates)

    def test_dates(self):
        actual_dates, actual_mid_rates = self.student_function(self.swap_rates)
        self.assertEqual(self.expected_dates, actual_dates)

    def test_mid_rates(self):
        actual_dates, actual_mid_rates = self.student_function(self.swap_rates)
        np.testing.assert_almost_equal(self.expected_mid_rates, actual_mid_rates)


class CalculateEmpiricalSurvivalProbabilitiesTest(TestCase):

    number_of_samples = 1000
    lambdas = 0.004
    last_year = 30
    
    def __init__(self, testname, student_function):
        super(CalculateEmpiricalSurvivalProbabilitiesTest, self).__init__(testname)
        self.student_function = student_function

    def test_size_must_be_30(self):
        actual_probabilities = self.student_function(self.number_of_samples, self.lambdas, self.last_year)
        self.assertEqual(actual_probabilities.size, 30)
        
    def test_probabilities(self):
        np.random.seed(218423)
        expected_probabilities = solutions.CalculateEmpiricalSurvivalProbabilities(self.number_of_samples, self.lambdas, self.last_year)
        np.random.seed(218423)
        actual_probabilities = self.student_function(self.number_of_samples, self.lambdas, self.last_year)
        np.testing.assert_almost_equal(expected_probabilities, actual_probabilities)