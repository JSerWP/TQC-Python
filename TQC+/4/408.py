even=0
odd=0
for i in range(10):
    num=int(input())
    if(num%2==0):
        even+=1
    else:
        odd+=1
    
print("Even numbers: {:}".format(even))
print("Odd numbers: {:}".format(odd))