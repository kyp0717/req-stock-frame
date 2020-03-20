import time
import statsmodels.api as sm 
from scipy import stats
from typing import Tuple, List, Dict
import behavior as bh
import algo
import timeSeries as tsr

## helper function to be used with pandas apply
def linearRegress(x):
    lr = stats.linregress(x['timepoint'].astype(int), x['price'].astype(float))
    return lr.slope

## New Function
Portfolio: List[Tuple[ticker, algo]]
def reconcile(p: Portfolio) -> Portfolio:
    pos = getPosition(conn)

ticker: str
position: List[ticker]
def getPosition(ibxConnn) -> position:
    pass

## New Function
## This function is a side affect
## It will execute the algo and return nothing
## No need to define type
def triage(p: Portfolio, conn) -> Portfolio:
    pnlList = getPnl()
    for tk, pnl in pnlList:
        if pnl < -0.05:
            sell(pk)
    # synchronize portfolio and algo list
    p2 = reconcile(p)
    return p2

   
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
    mktslope = mktData.groupby('ticker').apply(linearRegress)

    ## assess market condition at market and sector level
    mktBh = bh.AssessMarket(mktslope)
    sectorBh = bh.AssessSector(mktslope)

    ## find the algo type base on the market and sector condition
    algotype = deriveAlgo(mktBh, sectorBh)
    ## combine the stock and algo to generate a function
    algoFn = buildAlgo(algotype, stablStock)

    ## add algo to portfolio
    pfl = pfl.addAlgo(algoFn)

    # all algos will make 2 decisions: keep or sell the stock
    # rerun all algo in the portfolio
    runAlgos(pfl)


    



