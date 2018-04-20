from string import ascii_lowercase


def safe_pawns(pawns):
    count=0
    for a in pawns:
        print(a)
        need1 =ascii_lowercase [ascii_lowercase.find(a[0])-1]+ str(int(a[1])-1)
        need2 = ascii_lowercase [ascii_lowercase.find(a[0])+1]+ str(int(a[1])-1)

        print(need1,need2   )
        if need1 and need1 in pawns or  need2   and need2 in pawns:
            count+=1
    return(count)




# safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})

# safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")