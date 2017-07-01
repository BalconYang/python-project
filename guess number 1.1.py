number=8
print"guess me"
bingo=False
while bingo==False:
    answer=input()
    if answer＜number:
        print"too small"
    if answer＞number:
        print"too big"
    if answer=number:
        print"bingo"
#注意缩进        
