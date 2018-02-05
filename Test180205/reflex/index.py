
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
backend=__import__("backend."+lista[0])
print(backend.__name__)
tmpgetattr = getattr(backend,lista[0])
print(tmpgetattr.__name__)
afun = getattr(tmpgetattr,lista[1])
print(afun.__name__)
afun()



