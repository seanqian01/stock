import ccxt
print(ccxt.exchanges)
bittrex_test = ccxt.bittrex()
'''
可以联通的交易所有
bitflyer,bittrex,ftx,kraken,xena,
'''
Stock = "BTC/USD"
print(bittrex_test.fetch_ticker(Stock))
print(bittrex_test.urls)



