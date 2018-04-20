import  string
from functools import reduce
def find_message(text):
    if [x for x in text if x in string.ascii_uppercase] != []:
        text2 =  reduce(lambda x,y:x+y ,    [x for x in text if  x in string.ascii_uppercase]  )
        return (text2)
    else:
        return ""


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")