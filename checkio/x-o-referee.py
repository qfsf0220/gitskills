from     functools import reduce
def checkio(game_result: list) -> str:
    a,b,c=[x for x  in game_result]
    sa,sb,sc = [  reduce(lambda x,y:x+y,x) for  x  in  [x for x in zip(a,b,c)]]
    print(sa,sb,sc)
    x1=a[0]+b[1]+c[2]
    x2=a[2]+b[1]+c[0]
    print(x1,x2)
    listall =([a,b,c,sa,sb,sc,x1,x2])

    if "XXX" in listall :
        return("X")
    elif "OOO" in listall   :
        return("O")
    else:
        return("D")

        # if i =="XXX" or i =="OOO" :
        #     print(i[0])
        #     return(i[0])
        # else:
        #     print( "D")
        #     return( "D")

    # if a[0]==b[1]==c[2]:
    #     print (a[0])
    # if a[2] ==b[1] ==c[0]:
    #     print  (a[2])

checkio([
        "OO.",
        "XOX",
        "XOX"])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

