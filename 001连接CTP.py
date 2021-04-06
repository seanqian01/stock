'''backtest
start: 2021-01-17 09:00:00
end: 2021-02-15 15:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_CTP","currency":"FUTURES"}]
'''

# !python3
def main():
    while True:
        if exchange.IO("status"):
            exchange.SetContractType("rb2106")
            ticker = exchange.GetTicker()
            account = exchange.GetAccount()
            Log("rb2106 ticker:", ticker)
            Log("账户信息：", account)
            LogStatus(_D(), "已经连接CTP ！")
        else:
            LogStatus(_D(), "未连接CTP ！")

    def init():
        Log("初始化！")
