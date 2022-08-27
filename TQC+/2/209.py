x=int(input())
y=int(input())

d=((x-5)**2+(y-6)**2)**0.5
if(d<=15):
    print("Inside")
else:
    print("Outside")