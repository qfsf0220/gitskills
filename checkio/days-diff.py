import datetime
def days_diff(date1, date2):
    a1,b1,c1=date1
    a2,b2,c2 = date2
    time= (datetime.date(a1,b1,c1) - datetime.date(a2,b2,c2) ).days
    return(abs(time))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
