def compute(a,x,y):
    for i in range(y):
        for j in range(x):
            print("{:} ".format(a),end="")
        print()

a=input()
b=int(input())
c=int(input())
compute(a,b,c)