
import enum


### Market Class
@unique
class Behavior(enum.Enum):
    random: 1
    nonrandom: 2
    uncertain: 3

def assessMarket(mktTS: MarketTS) -> Behavior:
    pass


###  Sector Class
@unique
class Sector:
    healthcare: 1
    technology: 2
    ...

def findSector(tk: ticker) -> Sector:
    pass

def assessSector(s: Sector) -> Behavior:
    pass






