# -*- coding: utf-8 -*-
import random
print "if you don't know what to choose\n let me help you"
n = input("please enter 0 for help \nor\nplease enter 1 to hear yourself.\n> ")
if n == 0:
    a = input("enter a number you love that between 1 to 10\n> ")
    b = random.randint(1, 10)
    print "computer choose", b
    if a < b:
	    print "just try it, good luncky."
    else:
	    print "dont't try it.\nmaybe you have yourself choose now, \nwhy dont't to face it brave?"

if n == 1:
	print "good luncky"

