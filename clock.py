import time
import fmz
class AlarmClock:
    def __init__(self,triggerHour,triggerMinute):
        self.isTrigger = False
        self.TriggerHour = triggerHour
        self.TriggerMinute = triggerMinute
        self.nowDay = time.localtime(time.time()).tm_wday

    def Check(self):
        t =time.localtime(time.time())
        hour = t.tm_hour
        minute = t.tm_min
        day = t.tm_wday

        if day !=self.nowDay:
            self.isTrigger = False
            self.nowDay = day

        if self.isTrigger == False and hour == self.TriggerHour and minute >= self.TriggerMinute:
            self.isTrigger = True
            return True

        return False


def main():
    t1 = AlarmClock(14, 58)
    t2 = AlarmClock(9, 0)
    while True:
        if exchange.IO("status"):
            LogStatus(_D(), "已经连接！")
            exchange.SetContractType("rb2105")
            ticker = exchange.GetTicker()
            if t1.Check():
                Log("收盘", "#FF0000")

            if t2.Check():
                Log("开盘", "#CD32CD")
        else:
            LogStatus(_D(), "未连接！")
        Sleep(500)