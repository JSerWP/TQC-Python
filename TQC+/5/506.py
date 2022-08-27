def compute(a,b,c):
    k=b**2-4*a*c
    if(k<0):
        return "Your equation has not root."
    else:
        return str((-b+k**0.5)/2*a) +","+ str((-b-k**0.5)/2*a)

a=int(input())
b=int(input())
c=int(input())
print(compute(a,b,c))