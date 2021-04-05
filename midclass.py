# 我们需要获取数据，但是需要时间间隔获取
# 我们需要容错
# 一些数据的处理不需要放到逻辑层里
class midclass():
    def __init__(self):
        '''
        初始化数据
        '''
        pass
    def get_account(self):
        '''
        :获取账户信息:
        '''
        pass
    def get_ticker(self):
        '''
        :获取市价信息:
        '''
        pass
    def get_deepth(self):
        '''
        :return: 获取深度信息
        '''
        pass
    def get_ohlc_data(self):
        '''
        :return: 获取K线信息
        '''
        pass
    def create_order(self):
        '''
        :return: post一个挂单信息
        '''
        pass

    def cacel_order(self):
        '''
        :return: 取消挂单信息
        '''
        pass

    def refresh_data(self):
        '''
        :return: 刷新信息
        '''
        pass
