import time
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
