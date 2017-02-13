a=(x*x for x  in range(10000))

i=0
while True:
    if i==5001:
        try:
            print(next(a))
        except StopIteration:
            break
    else:
        try:
            next(a)
        except StopIteration:
         break
    i+=1
