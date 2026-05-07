# List Comprehension Practice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares of numbers
squares = [x ** 2 for x in numbers]

# Even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

# Odd numbers
odd_numbers = [x for x in numbers if x % 2 != 0]

print("Original List:", numbers)
print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)