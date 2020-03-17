
import behavior
import enum
import selectStock
import algos

algoFuncs = {
    AlgoType.Random: algos.randomFn
    sampleAlgo,
    otherAlgo }


@unique
class AlgoType(enum.Enum):
    random: 1
    nonrandom: 2
    grayzone: 3

def sampleAlgo(ticker):
    pass


    sampleAlgo.ticker = ticker # < you can do this
## random algo
def randomAlgo(tk: ticker) -> Function:
    pass

def nonRandomAlgo():
    pass

## derive algo base on market condition
def deriveAlgo(mkt: MarketBehavior, sector: SectorBehavior) -> AlgoType:
    pass

def buildAlgo(a: AlgoType, stk: findStkFn) ->  AlgoFn:




    

    #func()
    fn = partial(algoFuncs[algoType], stk)
    fn.AlgoType = a
    fn.Stock = stk
    return fn

fn = buildAlgo(at, "AAPL")




def addAlgo(agf: AlgoFn, p: Portfolio) -> Portfolio:
    return Portfolio.append(AlgoFn)

## New Function
## This function is a side affect
## It will execute the algo and return nothing
## No need to define type
def runAlgo(p: Portfolio) -> None:
    for algo in p:
        algo()











