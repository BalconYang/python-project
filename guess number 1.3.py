# -*- coding: utf-8 -*-
def isEqual(num1, num2):
  if num1 < num2:
    print"too small"
    return False
  if num1 > num2:
    print"too big"
    return False
  if num1 == num2:
    print"bingo"
    return Ture
  
  
isEqual(1, 3)
isEqual(3, 1)
isEqual(3, 3)
# 测试自定义函数

from random import randint
num = randint(1, 3)
print"guess number"
bingo = False
while bingo == False:
    answer = input()
    bingo = isEqual
  
  
# tips:定义函数def
  
