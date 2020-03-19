#! /usr/bin/env python3
import asyncio
from aiohttp import ClientSession
import stock_info
import pandas as pd
import time

# ask Chris why I cannot see base_url variable
base_url = stock_info.base_url
async def reqPrice(ticker:str, session) :
    'Get price, volume, and previous close for ticker'
    response = await session.get(base_url + ticker)
    data =  await response.json()
    price = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
    return ticker, price

async def gatherPrices(tickers:list):
    'Get price, volume, and previous close for all items in tickers list'
    async with ClientSession() as session:
        tasks = []
        for tick in tickers:
            tasks.append(reqPrice(tick, session))
        results = await asyncio.gather(*tasks)
    return results

def buildTimeSeries(tickers:list, timepoints = 4, delay = 2) -> pd.DataFrame:
    'get data for tickers list and run time series analysis for x timepoints'
    df = pd.DataFrame(columns=[
            'timepoint',
            'ticker',
            'price'
            ] )
    for tp in range(timepoints):
        results = asyncio.run(gatherPrices(tickers))
        for ticker, price in results:
            df = df.append({
                    'timepoint': tp,
                    'ticker': ticker,
                    'price': price  }, ignore_index=True)

        # df = df.append(additions)
        time.sleep(delay)
    # return df.pivot_table(index="ticker", columns="timepoint")
    return df

# stxlist = ['AAPL','AMZN']
# res = asyncio.run(gatherPrices(stxlist))
# print(res)
# tmp = buildTimeSeries(stxlist)
# print(tmp)
