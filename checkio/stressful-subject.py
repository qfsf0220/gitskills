import  string,re
def is_stressful(subj):
    needletter = (re.sub(r'[^helpasapurgent ]','',subj.lower()))
    needlist=[]
    needlist.append(needletter)
    print(needlist)
    tmplist=[]

    for i in range(len(needlist[0])-1):
        if needletter[i] != needletter[i+1]:
            tmplist.append(needletter[i])
    tmplist.append(needletter[-1])

    result = ''.join(tmplist)
    print(result)

    flag=False
    flag2=False

    has3gantan= subj.endswith("!!!")
    isUpall = [x for x in filter (lambda  x : x in string.ascii_lowercase,subj) ]

    Redlist =["help","asap","urgent"]
    hasRed = [ x for x  in   filter( lambda x :x.lower() in Redlist,subj.split(' '))           ]

    for i in Redlist:
        if needlist[0].find(i)!= -1:
            flag=True
    for i in Redlist:
        if result.find(i) != -1:
            flag2=True

    if isUpall == [] or has3gantan or hasRed !=[] or flag or flag2:
        return(True)
    else:
        return (False)


#
# is_stressful("I neeed HELP")
# print("--------------------==")
# is_stressful("h!e!l!p")
# print("--------------------==")
# is_stressful("We need you A.S.A.P.!!")
is_stressful("UUUURGGGEEEEENT here")
is_stressful("Hello puppy")

# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert is_stressful("Hi") == False, "First"
#     assert is_stressful("I neeed HELP") == True, "Second"
#     print('Done! Go Check it!')