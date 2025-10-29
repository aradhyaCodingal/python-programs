print("please select the operation")
print("1. add")
print("2. divide")
print("3. multiply")
print("4. substract")
num1=int(input("enter the 1st no."))
num2=int(input("enter the 2nd no."))
ch=int(input("enter your choice"))
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b
if ch==1:
    print(num1," + ",num2," = ",add(num1,num2))
elif ch==2:
    print(num1," / ",num2," = ",divide(num1,num2))
elif ch==3:
    print(num1," * ",num2," = ",multiply(num1,num2))
elif ch==4:
    print(num1," - ",num2," = ",sub(num1,num2))

