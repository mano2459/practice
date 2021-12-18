import pickle as pk

data = {}

f = open("binary/data1.dat", "rb")

try:
    while True:
        read_data = pk.load(f)

        print(read_data)

except EOFError:
    print("err...")
