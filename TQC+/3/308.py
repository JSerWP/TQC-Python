a=int(input())

for i in range(a):
    n=input()
    tmp=0
    for j in range(len(n)):
        tmp+=int(n[j])
    print("Sum of all digits of {:} is {:}".format(n,tmp))
