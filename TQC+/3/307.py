n=int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print("{:<2d}* {:<2d}= {:<4d}".format(j,i,j*i),end="")
        if(j==n):
            print()
    