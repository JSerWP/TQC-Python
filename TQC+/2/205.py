a=input()

if(a.isalpha()==True):
    print("{:} is a alphabet.".format(a))
elif(a.isdigit()==True):
    print("{:} is a number.".format(a))
else:
    print("{:} is a symbol.".format(a))