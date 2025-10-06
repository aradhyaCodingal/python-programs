d = int(input("Enter a decimal number: "))

og= d

b = ""

if d == 0:
    b = "0"
else:
    while d > 0:
        r = d% 2
        b = str(r) + b
        d = d// 2


print(f"Binary of {og} is {b}")