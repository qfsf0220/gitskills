def cums(data):
    if (data  [:-1]) ==[]:
        return data
    ret = cums(data[:-1])
    ret.append(ret[-1] + data[-1])
    print(ret)
    return ret


def checkio(data):
    a=cums(data)
    return (a[-1])




checkio([1,2,3,4,5])