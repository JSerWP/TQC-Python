x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())

d=((x1-x2)**2+(y1-y2)**2)**0.5

print("({:},{:})".format(x1,y1))
print("({:},{:})".format(x2,y2))
print("Distance = {:.4f}".format(d))