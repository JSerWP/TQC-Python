while(True):
    h=float(input())
    if(h==-9999):
        break
    w=float(input())
    if(w==-9999):
        break

    bmi=w/((0.01*h)**2)
    print("BMI: {:.2f}".format(bmi))

    if(bmi<18.5):
        print("under weight")
    elif(18.5<=bmi<25):
        print("normal")
    elif(25.0<=bmi<30):
        print("over weight")
    elif(bmi>=30):
        print("fat")
    