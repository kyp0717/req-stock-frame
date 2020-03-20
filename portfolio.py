
## New Function
Portfolio: List[Tuple[ticker, algo]]
def reconcile(p: Portfolio) -> Portfolio:
    pos = getPosition(conn)

ticker: str
position: List[ticker]
def getPosition(ibxConnn) -> position:
    pass

## New Function
## This function is a side affect
## It will execute the algo and return nothing
## No need to define type
def triage(p: Portfolio, conn) -> Portfolio:
    pnlList = getPnl()
    for tk, pnl in pnlList:
        if pnl < -0.05:
            sell(pk)
    # synchronize portfolio and algo list
    p2 = reconcile(p)
    return p2


