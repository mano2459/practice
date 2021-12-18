n = 5
i = 1
a = 0
b = 1
print("a=",a,"b=",b,"i=,",i)

while i < n:
    print("loop start.")
    
    print(a)
    c = a+b
    a = b
    b = c
    i = i+1

    print("a=",a,"b=",b,  "c=",c,"i=,",i)
