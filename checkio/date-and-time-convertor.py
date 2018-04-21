import datetime,re
def date_time(time):
    a=(re.split('[. :]',time))
    aa =datetime.datetime.strftime(datetime.datetime(2018, int(a[1]), 1, 1, 1,1, 1),"%B")
    if a[3]=='01' or a[4]=="01":
        return(str(int(a[0]))+' '+aa+" "+a[2]+" year "+str(int(a[3]))+ " hour " +str(int(a[4]))+" minute" )
    else:
        return(str(int(a[0]))+' '+aa+" "+a[2]+" year "+str(int(a[3]))+ " hours " +str(int(a[4]))+" minutes" )

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
