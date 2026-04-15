import math

# Taking input
angle = float(input("Enter angle in degrees: "))

# Converting degrees to radians
radians = math.radians(angle)

# Calculating values
sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

# Displaying results
print("Sin value:", sin_value)
print("Cos value:", cos_value)
print("Tan value:", tan_value)