x=int(input())

if(x%3==0 and x%5==0):
    print("{:} is a multiple of 3 and 5.".format(x))
else:
    if(x%3==0):
        print("{:} is a multiple of 3.".format(x))
    elif(x%5==0):
        print("{:} is a multiple of 5.".format(x))
    else:
        print("{:} is not a multiple of 3 or 5.".format(x))