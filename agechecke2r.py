
age = int(input("Enter your age: "))


if age <= 0:
    print("Invalid age! Age must be greater than 0.")

else:
    print("Valid age entered.")


    if age % 2 == 0:
        print("The age is EVEN.")
    else:
        print("The age is ODD.")