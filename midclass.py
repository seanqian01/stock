# 我们需要获取数据，但是需要时间间隔获取
# 我们需要容错
# 一些数据的处理不需要放到逻辑层里
from fmz import *
class midclass():
    def __init__(self,that_exchange):
        '''
        初始化数据
        '''
        self.exchange = that_exchange
        self.name = self.exchange.GetName()
        self.jyd = self.exchange.GetCurrency()

        pass
    def get_account(self):
        '''
        :获取账户信息:
        '''
# 先清空数据
        self.Balance = '___'
        self.Amount = '___'
        self.FrozenBalance ='___'
        self.FrozenStocks = '___'

# 获取账户信息
        try:
            self.account = self.exchange.GetAccount()
            self.Balance = self.account['Balance']
            self.Amount = self.account['Stocks']
            self.FrozenBalance = self.account['FrozenBalance']
            self.FrozenStocks = self.account['FrozenStocks']
            return True
        except:
            return False

    def get_ticker(self):
        '''
        :获取市价信息:
        '''
# ticker信息一般不用清空。因为TICKER需要定时获取。
        try:
            self.Ticker = self.exchange.Getticker()

            self.High = self.Ticker['High']
            self.Low = self.Ticker['Low']
            self.Sell = self.Ticker['Sell']
            self.Buy = self.Ticker['Buy']
            self.Last = self.Ticker['Last']
            self.Volume = self.Ticker['Volume']
            return  True
        except:
            return False


    def get_deepth(self):
        '''
        :return: 获取深度信息
        '''
        self.Ask = '___'
        self.Buy = '___'
        try:
            self.Depth = self.exchange.GetDepth()
            self.Ask = self.Depth['Asks']
            self.Buy = self.Buy['Buy']
            return  True
        except:
            return  False

    def get_ohlc_data(self,period):
        '''
        :return: 获取K线信息,15分钟
        '''
        self.ohlc_data = self.exchange.GetRecords(period)

    def create_order(self,order_type,price,amount):
        '''
        :return: post一个挂单信息
        '''
        if order_type == 'Buy':
            try:
                order_id = self.exchange.Buy(price, amount)
            except:
                return False

        elif order_type == 'Sell':
            try:
                order_id = self.exchange.Sell(price, amount)
            except:
                return True
        return order_id

    def cacel_order(self,order_id):
        '''
        :return: 取消挂单信息
        '''
        return  self.exchange.CancelOrder(order_id)

    def refresh_data(self):
        '''
        :return: 刷新信息
        '''
        if not self.GetAccount():
            return 'false get account'
        if not self.GetTicker():
            return 'false get ticker'
        if not self.Getdepth():
            return 'false get depth'
        if not self.Get_ohlc_data():
            return 'false get ohlc data'
        return 'refeash finished!!!'


def main():
    test_mid = midclass(exchange)
    Log(test_mid.get_account())
    Log(test_mid.refresh_data())
    Log(test_mid.get_ticker())