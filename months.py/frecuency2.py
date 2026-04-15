
d = {'codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'coding': 1}

value = int(input("Enter the value to check frequency: "))

count = 0

for v in d.values():
    if v == value:
        count += 1

print("Frequency of", value, "is:", count)