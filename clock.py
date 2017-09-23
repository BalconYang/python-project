# -*- coding: utf-8 -*-
import time
i = 1
while i:
    dt = list(time.localtime())
    hour = dt[3]
    minute = dt[4]
    if hour == 19 and minute == 23:
        print 'bingo'
        i = 0
