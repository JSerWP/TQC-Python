n=0
c=0
t=0

for i in range(5):
    k=int(input())
    if(k==1):
        n+=1
    elif(k==2):
        c+=1
    else:
        t+=1

    
    print("Total votes of No.1: Nami = {:}".format(n))
    print("Total votes of No.2: Chopper = {:}".format(c))
    print("Total null votes = {:}".format(t))

if(n>c):
    print("=> No.1: Nami won the election.")
elif(c>n):
    print("=> No.2: Chopper won the election.")
elif(c==n):
    print("=> No one won the election.")