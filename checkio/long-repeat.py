from  collections import Counter
def long_repeat(line):
    # result=(Counter(line).most_common(1)[0][1]) if line!='' else 0
    # print(result)
    # return result
    if  line != "":
        aa=[]
        parten = line[0]
        count=1
        for i in line[1:]:
            if i == parten:
                count+=1
            else:
                aa.append(parten+str(count))
                parten=i
                count=1
        aa.append(parten+str(count))
        print(aa)
        print(sorted(aa,key=lambda x:x[1],reverse=True)[0][1])
        return int(sorted(aa,key=lambda x:x[1],reverse=True)[0][1])
    else :
        return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

