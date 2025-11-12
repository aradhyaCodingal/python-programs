try:
    a=int(input("entera number"))
    b=int(input("enter a number"))
    print(a/b)
except ZeroDivisionError:
    print("divide by 0")
except ValueError:
    print("value error")
finally:
    print("it is a finally block")













