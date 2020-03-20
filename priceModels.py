#! /usr/bin/env python3

from scipy import stats
from collections import OrderedDict
import priceModels


## helper function to be used with pandas apply
def linearRegress(x):
    lr = stats.linregress(x['timepoint'].astype(int), x['price'].astype(float))
    return lr.slope


MktData: pd.DataFrame
MktSlope: pd.DataFrame
def regress(df: MktData) -> MktSlope:
    mktSlope = mktData.groupby('ticker').apply(pm.linearRegress)
    return mktSlope

    


def regress_old(df):
    'Pivot dataframe and append regression info'

    def calc(row):
        r = stats.linregress(timepoints, y=row)
        return pd.Series(oDict((
            ('change', row.iloc[-1] - row.iloc[0]), # change from first to last timepoint
            ('slope', r.slope),
            ('rvalue', r.rvalue),
            ('pvalue', r.pvalue),
            ('stderr', r.stderr),
            )))

    timepoints = df.columns.values # y values for regression
    results = prices.apply(calc,axis=1) # apply price regression
    print(results)
    return results

