a=lambda x,y :zip(x,y)

abc = iter(a([1,2,66,7,8,11,345,4,23,234,44],[3,5,55,6,9,23,4,54,345,3]))

def outzip(n):
    b = 1
    for i in range(10000):
        if b==n:
            try:
                print(next(abc))
            except StopIteration:
                break
        else:
            try:
                next(abc)
            except StopIteration:
                break
        b+=1

if __name__ == '__main__':
    outzip(8)