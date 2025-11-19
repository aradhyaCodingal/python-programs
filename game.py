import random 
playing =True 
num = str(random.randint(10,15))
print("try to guess number it will generate")

while playing:
    guess = input("give the guess:")
    if num==guess:
        print("correct")
        break
    else:
        print("wrong")
