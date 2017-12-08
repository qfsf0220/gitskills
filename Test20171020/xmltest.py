from xml.etree import ElementTree as ET
import  sys
# guanjianzi = sys.argv[1]
tree = ET.parse("C:\\Users\\Administrator\\SimulatorCfg3.xml")

root= tree.getroot()
dict1={}
for a in root:
    if a.tag=="Relay":
        # print(a.tag,a.attrib)
        for b in a:
            # print(b.tag+":")
            for c in b:
                # print(c.tag)
                for d in c.iter("Address"):
                    key=(c.tag+"|"+d.tag+":"+d.text)
                    # print(key)
                for e in c.iter("Queue"):
                    for f in e.iter("Name"):
                        value=(f.tag+":"+f.text)
                    for f2 in e.iter("Type"):
                        value2=value+" "+f2.tag+":"+f2.text
                        dict1[key]=value2

alist=[]
for i,j in dict1.items():
    if "fx" in j:
        x= (i+" "+j)
        alist.append(x)

dlist=sorted(alist)
blist=[]

num = int(len(dlist)/2)
a=0
for i in range(num):
    blist.append(dlist[a+num]+"    "+dlist[a])
    a+=1
for i in blist:
    print(i)

