import re,string

def checkio(data):
    flag1 = flag2 = flag3 =False
    if 10 <= len(data)<=64:
        for i in data :
            if i in string.ascii_lowercase :
                flag1 =True
            if i in string.digits:
                flag2=True
            if i in   string.ascii_uppercase:
                flag3=True
    if flag1 and  flag3 and   flag2:
        return True
    else:
        return False


#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('ULFFunH8ni') == True, "7th example"
    assert checkio('erer798rew9rew9r7ew987rw') == False, "8th example"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")