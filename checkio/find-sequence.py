import numpy
import re
from functools import reduce
def checkio(matrix):
    totallist= []
    for i in matrix:
        a=reduce(lambda x,y:str(x)+str(y),i)
        totallist.append(a)


    aa=numpy.array(matrix)
    for i in range(len(matrix)):
        totallist.append(  reduce( lambda x,y:str(x)+str(y),   aa[:,i])  )

    totallist.append ( reduce( lambda x,y:str(x)+str(y),   [matrix[i][i] for i in range(len(matrix))]) )

    totallist.append(  reduce( lambda x,y:str(x)+str(y)   ,[matrix[i][len(matrix)-i-1] for i in range(len(matrix))] )  )

    try:
        for j in range(1,len(matrix)-1):
            youshang =[matrix[i][i+j] for i in range(len(matrix)-j)]
            print(youshang)
            totallist.append( reduce(lambda x,y:str(x)+str(y),youshang))
        for j in range(1,len(matrix)-1):
            zuoxia = [matrix[i+j][i] for i in range(len(matrix)-j)]
            print(zuoxia)
            totallist.append( reduce(lambda x,y:str(x)+str(y),zuoxia))

        for j in range(2,len(matrix)):
            zuoshang =  [matrix[i][len(matrix)-i-j] for i in range(len(matrix)-j+1)]
            print(zuoshang)
            totallist.append( reduce(lambda x,y:str(x)+str(y),zuoshang))

        for j in range(1,len(matrix)-1):
            youxia =  [matrix[i+j][len(matrix)-i-1] for i in range(len(matrix)-j)]
            print(youxia)
            totallist.append( reduce(lambda x,y:str(x)+str(y),youxia))

    except IndexError as e:
        print(e)

    print(totallist)

    for i in totallist:
        if (re.findall(r'(\d)\1{3,}',i)) != []:
            return(True)
        else:
            continue
    return False

#
# checkio([
#         [1, 2, 1, 1],
#         [1, 1, 4, 1],
#         [1, 3, 1, 6],
#         [1, 7, 2, 5]
#     ])
#
#
# checkio([
#         [7, 1, 1, 8, 1, 1],
#         [1, 1, 7, 3, 1, 5],
#         [2, 3, 1, 2, 5, 1],
#         [1, 1, 1, 5, 1, 4],
#         [4, 6, 5, 1, 3, 1],
#         [1, 1, 9, 1, 2, 1]
#     ])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
