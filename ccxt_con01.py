from pprint import pprint

import ccxt
pprint(ccxt.exchanges)
ftx_test = ccxt.ftx()
'''
可以联通的交易所有
bitflyer,bittrex,ftx,kraken,xena,
'''
Stock = "BTC/USD"
pprint(ftx_test.fetch_ticker(Stock))
print(ftx_test.urls)



