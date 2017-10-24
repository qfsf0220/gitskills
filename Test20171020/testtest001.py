import time

nowtime = 877
while 1:

    if nowtime <880 and nowtime >845:
        print("almost 9 "+ str(nowtime))
    elif nowtime >900:
        print("xiaban "+str(nowtime))
    else:
        print("9-18 ing "+str(nowtime))
    nowtime+=1
    time.sleep(1);
