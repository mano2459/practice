import pickle as pk

stu ={}

f = open("binary/data1.dat","rb")

search_keys = [90]

try:
    print("searching......")
    while True:
        stu=pk.load(f)
        if stu[0] in search_keys:
            print(stu)
            found = True

except EOFError:
    if found == False:
        print('noop.....')

    else:
        print("success.....!")

    f.close()
