b = float(input("Enter the base number: "))
e = int(input("Enter the exponent (power): "))

result = 1

if e > 0:
    for _ in range(e):
        result *= b
elif e < 0:
    for _ in range(-e):
        result *= b
    result = 1 / result
else:
    result = 1  

print(f"\n{b} raised to the power of {e} is: {result}")