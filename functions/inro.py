# wap to enter datails and put it in a file.
def add():
    name = input("Enter your name : ")
    clas = input("Enter your class : ")
    roll = input("Enter your roll no.: ")
    mark = input('Enter your marks : ')

    f = open("functions/data1.txt","a")
    f.write(name+" ")
    f.write(clas+" ")
    f.write(roll+" ")
    f.write(mark)
    f.write("\n")

add()
add()
while True:
    add()

