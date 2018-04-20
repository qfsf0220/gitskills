def checkio(words):
    count=0
    for i in words.split(' '):
        if i.isalpha() :
            count+=1
        else:
            count =0
        if (count) >=3:
            return True
    return False

if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12")
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")