import pyautogui as pg
pg.FAILSAFE=False
print('关闭鼠标到屏幕最左面以后的错误提示')
pg.PAUSE = 0.5 #默认移动以后停顿时间是0.1秒 这里设置为0.5秒
#for i in range(10):
#	pg.moveRel(0,100,duration=0.15)
#	pg.moveRel(100,0,duration=0.15)
#	pg.moveRel(0,-100,duration=0.15)
#	pg.moveRel(-100,0,duration=0.15)
test= """
import pyautogui as pg

try:
    while True:
        x,y=pg.position()
        posStr= 'x: '+str(x).rjust(4)+' y: '+str(y).rjust(4)
        print(posStr,end='')
        print("\b"*len(posStr),end='',flush=True)
except KeyboardInterrupt:
    print("\nDone\n")
"""
print('''    ++>  x->
   (0,0).----------------->
        |
    ++  |
    y|  |
     |  |
     v  |
        |
        |
        v

''')

pg.moveTo(0,0,duration=0.2) #duration 位移时间
pg.moveRel(0,100)#以当前位置移动 0,100往下移动100个px
pg.moveRel(0,-100,duration=0.2)#网上
print('当前鼠标移动到 0,0')

c=pg.position() #获取鼠标位置

print(c)
#pg.doubleClick(button='left')#双击  左键 #方便的可以pg.rightClick()双击右键 pg.middleClick()双击中建  
#pg.mouseDown(button='right') #点下  右键
#pg.mouseUp( button='middle')#放开鼠标 中建

pg.click(c)
pg.click(10,10,button='right')
pg.moveTo(1000,50),pg.click()
pg.moveTo(1166,50)
pg.dragTo(1400,50,duration=0.25)
#pg.dragRel()  #以当前位置拖动

#############
import pyperclip  # 这个可以把数据保存到剪贴板
import functools
a=functools.reduce(lambda x,y:str(x)+'\n'+str(y),[ i for i in range(500)])
pyperclip.copy(a) #这里已经保存到剪贴板 可用notpad++黏贴 win自带文本不行》
#这里都是为 scroll 做准备  scroll 向上 scroll（负数） 向下滚动
import time
pg.click();time.sleep(3);pg.scroll(250)

##############屏幕处理
imagetest =pg.screenshot()
imagetest.getpixel( (0,0) ) #这里传入元祖 得到一个R G B 元组






