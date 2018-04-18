import numpy as np
import pandas as pd

def EuropeanOptionMC(forward, strike, discount_factor, time_to_maturity, volatility, number_of_samples, flag):
    standar_normal = np.random.randn(number_of_samples, 1)
    asset_at_maturity = forward * np.exp( -0.5*volatility**2*time_to_maturity + volatility*np.sqrt(time_to_maturity)*standar_normal )

    if flag == 1:
        simulated_option_price = discount_factor*(asset_at_maturity - strike).clip(0, np.inf)
    else:
        simulated_option_price = discount_factor*(strike - asset_at_maturity).clip(0, np.inf)

    return np.mean(simulated_option_price)

def ReadSwapRates(file, sheet, fromRow, columnRange):
    return pd.read_excel(file, sheet_name = sheet, skiprows = fromRow, usecols = columnRange)