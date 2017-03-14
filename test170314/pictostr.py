#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PIL import Image


imagename= 'luoji.jpg'
img = Image.open(imagename).convert('L')#转换为灰度模式
print(img.size)#打印图几 长宽
print(img.mode) #彩色 黑白 等
# print(img.save) #保存图片
# print(img.show) #打开图片
img2 = Image.open(imagename).convert('L')
# img.show()

w,h = img.size
if w>100:
    h= int( (100/w)*h/2)
    w=100

img = img.resize((w,h),Image.ANTIALIAS)

data = []
chars = [' ',',','1','+','n','D','@','M']
for i in range(0,h):
    line = ''
    for j in range(0,w):
            pi = img.getpixel((j,i))
            for k in range(0,8):
                if pi < (k+1) * 32:
                    line+=chars[7-k]
                    break
    data.append(line)
print(data)
file = open(imagename+'.txt','w')
for i in data :
    print(i,file=file)

file.close()

print("ok")



print(img.getpixel((99,9)))


