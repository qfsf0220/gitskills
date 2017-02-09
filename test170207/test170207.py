a = [x for x in range(10) if x%2==0]



b=map(lambda x:x,range(10))
for i in a:
    print(i,sep='~~',end=' ')

for i in b:
    print(i)
