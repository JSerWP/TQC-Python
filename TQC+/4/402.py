L=[]
while(True):
    n=int(input())
    if(n==9999):
        break

    L.append(n)

print(min(L))