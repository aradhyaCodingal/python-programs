attendence=int(input("enter your attendence"))
if attendence<75:
  mc=input("did you have any medical cause y / n")
    if mc=='y':
        print("allowed to write exam")
    elif mc=='n':
        print("no allowed to write exam")
    else:
        print("invalid input")
elif attendence>=75 and attendence<=100:
    print("you are allowed to write the exam")
else:
    print("invalid input")


