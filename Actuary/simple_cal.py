import numpy as np

def blackscholes_to_binomial(risk_free_rate,volatility,periods,years,dividend=0.0):
    """
    risk_free_rate: discount over years
    volatility: std
    periods: number of periods
    years: time T
    """
    r=np.expm1(risk_free_rate*years/periods)
    u=np.exp(volatility*np.sqrt(years/periods))
    d=1/u
    div=dividend*years/periods

    params = {
        "risk_free_rate":r,
        "upward_drift":u,
        "downward_drift":d,
        "dividend_per_period":div,
    }

    return params
