from collections import  Counter
import re
def popular_words(text, words):
    text_list= list(filter(lambda x: x != '', re.split('[\n ]', text.lower())))
    numdict = {}
    countall=Counter(text_list)
    for i in words:
        if i in countall.keys():
            numdict[i]= countall[i]
        else:
            numdict[i]=0

    return (numdict)


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")