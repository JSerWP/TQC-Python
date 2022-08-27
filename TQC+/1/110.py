import math
n=float(input())
s=float(input())

a=(n*s**2)/(4*math.tan(math.pi/n))
print("{:.4f}".format(a))