# 实现基本GUI功能
# -*- coding: utf-8 -*-
from Tkinter import*
from ScrolledText import ScrolledText

root = Tk()
root.title('hello')
text = ScrolledText(root, font=("微软雅黑", 10))
text.grid()
# 标题

button = Button(root, text="bingo", font=("微软雅黑", 10), fg="blue")
button.grid()
# 按钮

varl = StringVar()
label = Label(root, font=("微软雅黑", 10), fg="red", textvariable=varl)
label.grid()
varl.set("loading")
# 动态文字

root.mainloop()
