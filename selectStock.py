



stockList = getPreSelectedStocks()

### Analysis of Pre-Selected Stock List
### define stock characteristics
class StkBehavior:
    deltaPrevious: float
    deltaVolume: float

Stable: boolean

def isStkStable(sb: StkBehavior) -> Stable:
    pass


## class to capture stock stability list
class StkStability:
    stability: pd.DataFrame


###  Analysis of Sector
class SectorBehavior:
    



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

 
