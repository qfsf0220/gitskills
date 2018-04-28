def checkio(n, m):
    if n >m:
        twon=(bin(n).replace('b',''))
        twom=(bin(m).zfill(len(bin(n))).replace('b',''))
    else:
        twom=(bin(m).replace('b',''))
        twon=(bin(n).zfill(len(bin(m))).replace('b',''))

    return(len ([ x for x in  filter( lambda x :x[0]!=x[1] , [ x for x in (zip(twon,twom) )  ]  ) ] ) )

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
