import re
def checkio(expression):
    open_list=["{" ,"(","["]
    close_list = [ "}",")","]"]
    all_dict={')': '(', ']': '[', '}': '{'}
    a=[]
    tmplist=[]

    for i in range(len(expression)):
        if re.findall(r'[\{\}\[\]\(\)]',expression[i]):
            a.append(expression[i])
    print(a,"原始列表")

    if a != []:
        if a[0] in close_list:
               return( False)
        elif len(a) % 2 != 0:
            return (False)
        else:
            for i in range(len(a)):
                if a[i] in open_list:
                    tmplist.append(a[i])
                elif a[i] in close_list:
                    if all_dict[a[i]] == tmplist[-1]:
                        tmplist.pop()
            print(tmplist,"now")
            if tmplist ==[]:
                return(True )
            else:
                return(False)
    else:
        return True






# checkio("2+3")
# checkio("{[(3+1)+2]+}")
# checkio("[1+1]+(2*2)-{3/3}")
# checkio("(({[(((1)-2)+3)-3]/3}-3)")
# checkio("(3+{1-1)}")
# checkio("[1+202]*3*({4+3)}")
#
# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("[1+202]*3*({4+3)}") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
