def g():
    for i in "AVCXS":
        yield i

def g2():
    for i in range(1,17,3):
        yield i

for i in g2():
    print(i)


def g3():
    yield from "abcd"
    yield from  range(1,5)
lg3 = list(g3())
print(lg3)
print ([lg3[i:i+4]  for i in range(0,len(lg3),4)]  )

from collections import Iterable
def flattt(items,ignorpes=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable)and not isinstance(x,ignorpes):
            yield  from flattt(x)
        else:
            yield x
items = [1, 2, [3, 4, [5, 6], 7], 8]

print (   list (flattt(items) ))
items2 = ["qf",["sf"]]
print(  list (flattt(items2)))

from collections import namedtuple
Result = namedtuple('Result','con avera')

def averageinfo():
    total=0.0;
    count  =0;
    average=None
    while 1:
        term = yield #main 函数发送数据到这里
        if term is None:
            break
        total +=term
        count+=1
        average = total/count
    return Result(count,average)

def grouper(results,key):
    results[key]=yield from averageinfo()

def main(data):
    resulttt={}
    for key,value in data.items():
        group=grouper(resulttt,key)
        next(group)
        for i in value:
            group.send(value)
        group.send(None)
    repoert(resulttt)

def repoert(resultt):
    for key ,value in sorted(resultt.items()):
        group,unit = key.split(";")
        print('{:2} {:5} averaging {:.2f}{}'.format(resultt.count, group, resultt.average, unit))

data = {
    'girls;kg': [40, 41, 42, 43, 44, 54],
    'girls;m': [1.5, 1.6, 1.8, 1.5, 1.45, 1.6],
    'boys;kg': [50, 51, 62, 53, 54, 54],
    'boys;m': [1.6, 1.8, 1.8, 1.7, 1.55, 1.6],
}

if __name__ =="__main__":
    main(data)