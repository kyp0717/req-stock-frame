
import enum


### Market Class
@unique
class Behavior(enum.Enum):
    Random: 1
    SellOff: 2
    Rally: 3
    Unknown: 4

def assessMarket(mktTS: MarketTS) -> Behavior:



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






