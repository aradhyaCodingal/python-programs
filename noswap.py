
a = int(input("Enter first number : "))
b = int(input("Enter second number: "))
c = int(input("Enter third number : "))

print("Before swapping:")
print(f"number= {a} {b} {c}")

a, b, c = c, a, b

print("After swapping ""(a -> c, b -> a, c -> b)")
print(f"number= {a}{b}{c}")



