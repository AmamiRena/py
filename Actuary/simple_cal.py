from typing import Iterator
import numpy as np
import pandas as pd
from collections import Iterable

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

    params={
        "risk_free_rate":r,
        "upward_drift":u,
        "downward_drift":d,
        "dividend_per_period":div,
    }
    return params

def discount(time,r):
    if not isinstance(time,Iterable):
        discounts=(1+r)**(-time)
    else:
        discounts=pd.DataFrame([(1+r)**(-t) for t in time],index=time)
    return discounts

def present_value(flow,r,periods=None):
    if periods is None:
        periods=flow.index
        flow_index=flow
    else:
        flow_index=pd.Series(list(flow),index=periods)
    discounts=discount(periods,r)
    result=discounts.multiply(flow_index,axis='index').sum()
    return result

def duration(flow):
    total_flow=flow.sum()
    weights=flow/total_flow
    result=weights.T @ flow.index
    return result

def portfolio_return(weights,r):
    return weights.T@r

def portfolio_vol(weights,cov):
    return (weights.T@cov@weights)**0.5