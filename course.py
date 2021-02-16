import ccxt
print(ccxt.exchanges)
bitflyer_test = ccxt.bitflyer()
Stock = "BTC/USD"
print(bitflyer_test.fetch_ticker(Stock))



