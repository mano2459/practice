import pickle as pk


n = int(input("No. of entries you wanna enter : "))

with open ("binary/data1.dat", "ab")as f:
    for a in range(n):
        ent = [None, None, None]
        ent[0] = int(input("Roll no : "))
        ent[1] = input("Name : ")
        ent[2] = input("Marks : ")
        pk.dump(ent,f)
        print(".......................")

    pass

print("done....")