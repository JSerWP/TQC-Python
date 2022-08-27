def compute(n):
    a=0
    b=1
    for i in range(n):
        if(i<=1):
            print("{:} ".format(i),end="")
        else:
            k=a+b
            print("{:} ".format(k),end="")
            a=b
            b=k
            
n=int(input())
compute(n)
