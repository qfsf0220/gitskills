
a={}
a["name"]="yy"
a[1]="python"
a[2]="java"
a["name2"]=["dongwan","huafa","58"]

print(a)


b=(["name1","zk"],["name2","xxd"],["name3","ypq"])

print(dict(b))

c={}.fromkeys(("id","name"),"")
print(c)

print(dict(b).get('name2'))

x=[x for x in map(lambda x,y:x*y,[1,2,3,4],[2,3,4,5])]

print(x)