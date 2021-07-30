## Actuary Model_Pricing (mainly based on Exam MFE and C)
<font style="color:red" size=2.5>Some forCalc.py files may no longer be able to run due to the scripts modification.</font>.

### July 30th, 2021, night stalker version<br/>
- Implement blackscholes model with P&L hedge (call only) with lines of prices
- Implement credit default obligation and calculate tranche loss
- More functions are to be implemented
------------------------

### July 28th, 2021, night owl version<br/>
- Modify some functions within CAPM, allowing to calculate true expected capital return, which is to 'calculate new return on existing weights'
- Update Value-at-Risk(conditional or non-conditional)
------------------------
### July 25th, 2021<br/>
- Implement CAPM, including 3 main strategies: max sharpe ratio, equally weighted and global min var portfolio
- Can plot efficient frontier
------------------------
### July 24th, 2021 mid-night version<br/>
- Major Change
- Implement Annuity calculation, swaps pricing, Black-derman-toy rate model and pass through mortgage backed securitization(PSA)
- Add more functions on simple_cal toolkit: discounts, duration, present_value
------------------------
### July 21st, 2021<br/>
- Construct Binomial Tree structure
- Implement stockpricing, optionspricing, forwardpricing, futurepricing models
- interest rate can be done in stockpricing, just set S0 to corresponding parameters
