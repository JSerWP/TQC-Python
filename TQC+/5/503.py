def compute(a,b):
    tmp=0
    for i in range(a,b+1):
        tmp+=i
    return tmp
a=int(input())
b=int(input())
print(compute(a,b))