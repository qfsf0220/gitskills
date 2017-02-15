from multiprocessing import Process
from multiprocessing.pool import ThreadPool
# a=[]
# def hihi(j):
#     a.append (("hi"+j))
#     print(a)
# #
# # print((hihi("aa")))
# # print(a)
#
# if __name__ == '__main__':
#     for i in str(range(10)):
#         p=Process(target=hihi,args=(i,))
#         p.start()
def hi(i):
    a=("hi", i)
    return (a)
if __name__ == '__main__':
    for i in range(4):

        p=Process(target=hi,args=(i,))
        print(p)
        p.start()
