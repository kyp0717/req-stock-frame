
import enum
import statModels as sm
import timeSeries as ts
from typing import List

### Market Class
@unique
class Behavior(enum.Enum):
    Random: 1
    SellOff: 2
    Rally: 3
    Unknown: 4


@dataclass
class MarketStatus:
    Market: Behavior
    Sector: List[Behavior]



def assessMarket(mktSlope: MarketSlope) -> MarketStatus:





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






