num = int(input("Enter a number: "))
temp = (num)
count = 0
if temp == 0:
    count = 1
else:
    while temp > 0:
        temp = temp // 10 
        count += 1
        

print(f"Total digits in the number: {count}")
