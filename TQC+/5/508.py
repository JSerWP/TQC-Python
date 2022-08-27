def compute(x,y):
    r=x%y
    while(y!=0):
        r=x%y
        x=y
        y=r

    return x

x=int(input())
y=int(input())
print(compute(x,y))