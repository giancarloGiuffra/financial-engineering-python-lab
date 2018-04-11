import numpy as np

def EuropeanOptionMC(forward, strike, discount_factor, time_to_maturity, volatility, number_of_samples, flag):
    standar_normal = np.random.randn(number_of_samples, 1)
    asset_at_maturity = forward * np.exp( -0.5*volatility**2*time_to_maturity + volatility*np.sqrt(time_to_maturity)*standar_normal )

    if flag == 1:
        simulated_option_price = discount_factor*np.max(asset_at_maturity - strike, 0)
    else:
        simulated_option_price = discount_factor*np.max(strike - asset_at_maturity, 0)

    return np.mean(simulated_option_price)