from tkinter import  *

def printinfo():
    global a
    s= Label(a,text="fffff")
    s.pack()

a= Tk()
b1= Button(a,text="按钮1",command = printinfo)
b1.pack()

a.mainloop()
