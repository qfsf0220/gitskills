from collections import Counter

def checkio(text):
    text2=""
    letterlist=[]
    max = 0
    for i in text.lower():
        if i.isalpha():
            text2 += i
    a=Counter(text2)
    sorteddict= sorted(a.items(),key=lambda x:x[1],reverse=True)

    for i in sorteddict:
        if i[1]>=max:
            max =i[1]
            letterlist.append(i)
    sortedletterlist = sorted(letterlist,key=lambda x:x[0])
    return sortedletterlist[0][0]



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")