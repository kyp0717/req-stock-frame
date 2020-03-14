
from adt import adt, Case
from dataclasses import dataclass
import typing as T
import enum 

stockList = getPreSelectedStocks()

### Analysis of Pre-Selected Stock List
### define stock characteristics
class Behavior:
    prevClose: float
    beta: float


def isStkStable(stk: ticker) -> BehaviorStk:
    pass


##  Stock Class
@adt
class BehaviorStk:
    LATENT: Case 
    STABLE: Case
    ACTIVE: Case



    



## Stock Selection process
## Find the stock and corresponding algo
##
TradeStrategy: List[Tuple[ticker,algo]] 
def deriveTradeStrategy(sp: SP500) -> TradeStrategy:
    sectorStat = getSectorStat(marketStat)



## Find stock to trade
def findStock(p: sp500) -> ticker:
    betas = getBeta()
    avgVol = getAverageVolume()

 
