a=float(input())
b=float(input())
c=int(input())

print("Month\tAmount")
for i in range(1,c+1):
    a+=a*b/1200
    print("{:3d}\t{:.2f}".format(i,a))