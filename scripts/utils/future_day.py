# -*- coding: UTF-8 -*-
import datetime

class FutureDay:
    def days_ahead(self, weekday):
        d = datetime.datetime.now()
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0: # Target day already happened this week
            days_ahead += 7

        return days_ahead
        # return d + datetime.timedelta(days_ahead)

    def next_weekend(self, weekday):
        d = datetime.datetime.now()
        return d + datetime.timedelta(self.days_ahead(weekday))


if __name__ == "__main__":
    # 範例測試，距離最近的星期三有幾天＆最近的星期三是幾月幾號
    x = FutureDay()
    days_ahead = x.days_ahead(2) # 0 = Monday, 1 = Tuesday, 2 = Wednesday...
    print(days_ahead)

    next_weekend = x.next_weekend(2)
    print next_weekend.strftime("%Y%m%d")
