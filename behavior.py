
import enum
import statModels as sm
import timeSeries as ts
from typing import List, Dict

### Market Class
@unique
class Behavior(enum.Enum):
    Random: 1
    SellOff: 2
    Rally: 3
    Unknown: 6

@unique
class Trend(enum.Enum):
    Upturn: 1
    Downtuwn: 2

@dataclass
class MarketStatus:
    Market: Behavior
    Sector: Dict[Behavior]

def deriveBehavior(slopePct: float) -> Behavior:
    if slopePct < 0.20: 
        return Behavior.SellOff
    elif (slopePct >= 20 and slopePct < 0.40) or (slopePct > 0.60 and slopePct <= 0.80): 
        return Behavior.Unknown
    elif (slopePct >= 0.40 and slopePct <= 0.60):
        return Behavior.Random
    elif slopePct > 0.80:
        return Behavior.Rally


def assessMarket(slopeDF: MarketSlope) -> MarketStatus:
    slopePct = calcPctUpTick(slopeDF['slope'])
    mktbehavior = deriveBehavior(slopePct)
    






def calcPctUpTick(slopeDF: MarketSlope) -> float:
    pct = slopeDF['UpInd'].sum() / slopeDF['UpInd'].len()


    
    





###  Sector Class
@unique
class Sector(enum.Enum):
    healthcare: 1
    technology: 2
    ...

def findSector(tk: ticker) -> Sector:
    pass



def assessSector(s: Sector) -> Behavior:
    pass






