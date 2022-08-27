while(True):
    year=int(input())
    if(year==-9999):
        break
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                print("{:} is a leap year.".format(year))
            else:
                print("{:} is not a leap year.".format(year))
        else:
            print("{:} is a leap year.".format(year))
    else:
        print("{:} is not a leap year.".format(year))