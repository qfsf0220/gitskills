# -*- encoding:utf-8 -*-
import jieba

alist = jieba.cut("精精彩彩，羡慕各位",cut_all=True,HMM=False)
print(" ".join(alist))

blist = jieba.cut("精精彩彩 羡慕各位",cut_all=False,HMM=False)
print(" ".join(blist))

clist = jieba.cut("精精彩彩 羡慕各位",HMM=False)
print(" ".join(clist))

import matplotlib.pyplot as plt
import wordcloud

text = open("C:\\Users\\Administrator\\Desktop\\chartlog.txt").read()

wordlist_jieba = jieba.cut(text,cut_all=True)
word_split=" ".join(wordlist_jieba)

myw=wordcloud.WordCloud().generate(word_split)
plt.imshow(myw)
plt.axis("off")
plt.show()



# x=word_split.split(" ")
# print("+"*10+type(x).__name__)
# while '' in x:
#     x.remove('')
#
# while '\n' in x:
#     x.remove('\n')
#
# setx=set(x)
# print("*"*100)
# xxx=[]
# for i in setx:
#     xxx.append([i,x.count(i)])
# for i in range(10):
#     print(sorted(xxx,key=lambda x:x[1],reverse=True)[i])





