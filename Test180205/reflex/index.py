
#aaa/bbb

data = input("Enter:(aaa/bbb)")

lista=data.split('/')
#
# import Test180205.reflex.backend
# from  Test180205.reflex.backend import aaa
# if data =="aaa/a":
#     Test180205.reflex.backend.aaa.a()
# elif data=="aaa/b":
#     aaa.b()
print("*"*10)
backend=__import__("backend."+lista[0])#这个等于是父文件夹（如果有的话）
print(backend.__name__)
tmpgetattr = getattr(backend,lista[0])#这个等于程序所在文件夹（当前文件夹路径）参数一，父目录 参数二程序名
print(tmpgetattr.__name__)
afun = getattr(tmpgetattr,lista[1])#这个等于是程序 参数一 程序的相对路径（当前文件夹） 参数2 方法名
print(afun.__name__)
afun()



