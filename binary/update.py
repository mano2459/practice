import pickle as pk
stu={}
found = False

f = open("binary/data1.dat","rb+")

try:
    while True:
        pos = f.tell()
        stu = pk.load(f)

        if stu[0]==1:
            stu[0] = int(input("new roll = "))
            f.seek(pos)
            pk.dump(stu,f)
    
except:
    if found==True:
        print()

f.close()