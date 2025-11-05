def cube(number):
    return number * number * number

def cube_divisible(number):
 if number % 3 ==0:
    return cube(number)
 else:
  return False
 
print(cube_divisible(9))
print(cube_divisible(4))


