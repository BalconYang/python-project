# -*- coding: utf-8 -*-
print "Everyone is different,don't care,just for fun!\nTell me your name."
name = raw_input()

# 类似于用1，2代表男女如何实现？
sex = raw_input("sex，na1，nv2")
if sex == 1:
    print "handsome"
if sex == 2:
    print "beautiful"

print"month"
month = input()
print"day"
day = input()

if(month == 1 and 20 < day < 31)or(month == 2 and 1 < day < 18)and sex == 1:
    print "it's fun"
else:
    print str(name)+"you"+str(month)+str(day)+",you and live_fang see bright star together!"
