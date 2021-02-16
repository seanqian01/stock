import ccxt
print(ccxt.exchanges)
bitmax_test = ccxt.binance()
bitmax_test.fetch_ticker('BTC/USD')



