
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

def guessBehavior(slopeDF: MarketSlope) -> Behavior:


def assessMarket(slopeDF: MarketSlope) -> MarketStatus:
    pctUp = calcPctUpTick(slopeDF)
    if pctUp >= 0 and pctUp < 0.20: return



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






