print("select your ride")
print("1. bike")
print("2. car")
c1=int(input("enter your choice"))
if c1==1:
    print("select your bike")
    print("1. activa")
    print("2. honda")
    c2=int(input("enter your choice")) 
    if c2==1:
        print("user has selected activa as ride")
    elif c2==2:
        print("user has selected honda ")
elif c1==2:
    print("select your car")
    print("1. suzuki")
    print("2. nano")
    c3=int(input("enter your choice")) 
    if c3==1:
        print("user has selected suzuki as ride")
    elif c3==2:
        print("user has selected nano ")
else:
    print("invalid input")


    