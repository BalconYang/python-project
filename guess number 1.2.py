#coding=utf-8
from random import randint
print"guess me"
#answer=3
answer=randint(1,6)
bingo=False
while bingo==False:
  number=input()
  if answer＞number:
    print"too small"
  if answer＜number:
    print"too big"
  if answer＝＝number:
    print"bingo"
    bingo=Ture
