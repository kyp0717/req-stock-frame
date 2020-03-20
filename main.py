import time
import statsmodels.api as sm 
from scipy import stats
from typing import Tuple, List, Dict
import behavior as bh
import algo
import timeSeries as tsr
import priceModels as pm

   
market_close = datetime.datetime.now().replace(hour=16, minute=0) 
pfl = Portfolio[]
stkRandom = ['MSFT']
stkSellOff = ['MSFT']
stkRally = ['MSFT']

while datetime.datetime.now() < market_close:
    # first thing --- check pnl for each stock in portfolio
    # sell any stock with 5% or more loss:
    pfl = triage(pfl, ibxconn)

    # step 2: get the dataframe with 5 time points
    # use this list for now; implement stock seletion later
    mktData = tsr.buildTimeSeries()

    # perform regression to get market status
    mktSlope = tsr.regress(mktData)
    # mktSlope = mktData.groupby('ticker').apply(pm.linearRegress)

    ## assess market condition at market and sector level
    mktState = bh.AssessMarket(mktSlope)

    ## find the algo type base on the market and sector condition
    algotype = deriveAlgo(mktState)
    ## combine the stock and algo to generate a function
    algoFn = buildAlgo(algotype, stablStock)

    ## add algo to portfolio
    pfl = pfl.addAlgo(algoFn)

    # all algos will make 2 decisions: keep or sell the stock
    # rerun all algo in the portfolio
    runAlgos(pfl)


    



