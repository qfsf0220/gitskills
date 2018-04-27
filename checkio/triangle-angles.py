import math
def checkio(*args):
    if str(args[0]).isdigit():
        dlist=[x for x in args]
        print(sorted(dlist),"sotedlist")
        sortedlist = sorted(dlist)
    else:
        dlist=args[0]
        print(sorted(dlist),"sotedlist")
        sortedlist = sorted(dlist)

    a,b,c = sortedlist[0],sortedlist[1],sortedlist[2]

    if sortedlist[0] +sortedlist[1] <= sortedlist[2] :
        return ([0,0,0])

    elif sortedlist[0]  ==sortedlist[1] == sortedlist[2]:
        return ([60,60,60])
    elif sortedlist[0] +sortedlist[1] > sortedlist[2] and sortedlist[0]**2 +sortedlist[1]**2 == sortedlist[2]**2:
        jiao1=(round(math.degrees(math.acos(a / c))))

        jiao2= (round(math.degrees(math.acos(b / c))))

        jiao3= (180-jiao1-jiao2)
        return  (sorted([jiao1,jiao2,jiao3]))
    else:
        cosa =(b*b + c*c - a*a) /(2*b*c)
        cosb= (a*a+c*c - b*b) /(2*a*c)
        jiao1 = round( math.degrees  (math.acos ( cosa))  )
        jiao2 =   round(  math.degrees  (math.acos ( cosb)) )
        jiao3 = (180 - jiao1 - jiao2)
        return(sorted([jiao1, jiao2, jiao3]))

# checkio(4, 4, 4)
# #These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(11,20,30) == [11,20,149], "It's can not be a triangle"


