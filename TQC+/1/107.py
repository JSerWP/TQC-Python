from tkinter import E


a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())

s=a+b+c+d+e
avg=s/5

print("{:.1f} {:.1f} {:.1f} {:.1f} {:.1f}".format(a,b,c,d,e))
print("Sum = {:.1f}".format(s))
print("Average = {:.1f}".format(avg))