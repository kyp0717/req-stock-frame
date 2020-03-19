
import behavior
import enum
import selectStock
import algos

algoFuncs = {
    AlgoType.Random: algos.randomFn
    AlgoType.SellOff: algos.sellOffFn
    AlgoType.Rally: algos.rallyFn
    AlgoType.Uncertain: algos.uncertainFn
    }


@unique
class AlgoType(enum.Enum):
    Random: 1
    SellOff: 2
    Rally: 3
    Uncertain: 4


## derive algo base on market condition
def deriveAlgo(mkt: MarketBehavior, sector: SectorBehavior) -> AlgoType:
    pass

def buildAlgo(a: AlgoType, stk: findStkFn) ->  AlgoFn:
    #func()
    fn = partial(algoFuncs[algoType], stk)
    fn.AlgoType = a
    fn.Stock = stk
    return fn


def addAlgo(agf: AlgoFn, p: Portfolio) -> Portfolio:
    return Portfolio.append(AlgoFn)

## New Function
## This function is a side affect
## It will execute the algo and return nothing
## No need to define type
def runAlgo(p: Portfolio) -> None:
    for algo in p:
        algo()











