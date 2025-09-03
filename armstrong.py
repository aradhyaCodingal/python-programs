num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+(digit**3)
    temp=temp//10
print("the sum of cube of all number is",sum)
if sum==num:
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")
