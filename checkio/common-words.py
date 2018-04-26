def checkio(first, second):
    firstlist = first.split(',')
    secondlist = second.split(',')
    alist = sorted  (list(set(firstlist).intersection(set(secondlist)))  )

    reslut =(",".join(alist)) if alist!=[] else ""
    return  reslut


checkio("hello,world", "hello,earth")
checkio("one,two,three", "four,five,one,two,six,three")
checkio("one,two,three", "four,five,six")


#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio("hello,world", "hello,earth") == "hello", "Hello"
#     assert checkio("one,two,three", "four,five,six") == "", "Too different"
#     assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
