def compute(x):
    if(x<=1):
        return "Not Prime"
    else:
        for i in range(2,x):
            if(x%i==0):
                return "Not Prime"
        return "Prime"

x=int(input())
print(compute(x))