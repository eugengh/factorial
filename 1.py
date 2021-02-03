import sys
MAX_INT = sys.maxsize
x=1

while (x<MAX_INT):
    a=x
    s=0
    while a!=0:
        b = 1
        c = a % 10
        for i in range(1, c+1):
            b*=i
        s+=b
        a//= 10
    if s == x:
        print(x)
    x+=1
