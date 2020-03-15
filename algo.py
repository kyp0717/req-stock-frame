
import behavior
import enum
import selectStock







@unique
class AlgoType(enum.Enum):
    random: 1
    nonrandom: 2

## generate a function that with stock ticker inside
## this is a closure
class AlgoGenerator: 
    def __init__(self, ticker, algo):
        tk = ticker
        ag = algo

    def generate(tk, al):
        return def algofn:


## random algo
def randomAlgo(tk: ticker) -> Function:
    pass



## derive algo base on market condition
def derviveAlgo(mkt: MarketBehavior, sector: SectorBehavior) -> Algo:
    pass

def buildAlgo(a: Algo, stk: findStkFn) ->  AlgoFn:
    pass


def addAlgo(agf: AlgoFn, p: Portfolio) -> Portfolio:
    pass


## New Function
## This function is a side affect
## It will execute the algo and return nothing
## No need to define type
def runAlgo(p: Portfolio) -> None:
    pass










