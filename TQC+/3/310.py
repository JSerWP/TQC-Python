n=int(input())

tmp=0
for i in range(2,n+1):
    tmp+=1/((i-1)**0.5+i**0.5)

print("{:.4f}".format(tmp))