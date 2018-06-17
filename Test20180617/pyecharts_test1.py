import pyecharts

bar = pyecharts.Bar("That is it Now well done")

wuping= ["ant","bear","cat","dog","elephant","frog","gerala"]

v1 = [32,4,66,35,12,3,54]

v2 = [12,45,45,8,5,64,42]

if len(v1)==len(v2):


    bar.add("AA",wuping,v1,is_stack=True,mark_point=["max","average","min"])
    bar.add("BB",wuping,v2,is_stack=True,mark_line=["min","max"],is_convert=True)

    bar.render()
else:
    print("len error")


print([str(i)+"月" for i in range(1,13)])