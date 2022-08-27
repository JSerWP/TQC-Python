def compute(p,q):
    r=p%q
    while(q!=0):
        r=p%q
        p=q
        q=r
    return p

x=int(input())
y=int(input())
m=int(input())
n=int(input())
p=x*n+y*m
q=y*n
gcd=compute(p,q)
print("{:} / {:} + {:} / {:} = {:} / {:}".format(x,y,m,n,int(p/gcd),int(q/gcd)))
