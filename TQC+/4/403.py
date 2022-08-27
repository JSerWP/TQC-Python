from re import I


a=int(input())
b=int(input())

k=0
c=0
for i in range(a,b+1):
    if(i%4==0 or i%9==0):
        k+=1
        c+=i
        print("{:<4d}".format(i),end="")
        if(k%10==0):
            print()

print()
print("{:>4d}".format(k))
print("{:>4d}".format(c))

