char = input("Enter a single numeric character (0-9): ")
if len(char) == 1 and char.isdigit():
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is {ascii_value}.")
else:
    print("Invalid input. Please enter a single digit (0-9).")