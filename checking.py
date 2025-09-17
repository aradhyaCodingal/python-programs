ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter only one character.")
else:
    if ch.isalpha():
        print(f"'{ch}' is an Alphabet.")
    elif ch.isdigit():
        print(f"'{ch}' is a Number.")
    else:
        print(f"'{ch}' is neither a Number nor an Alphabet.")