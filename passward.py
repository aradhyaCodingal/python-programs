import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits

all_characters = lower + upper + numbers

password_length = 10

password = ""

for i in range(password_length):
    password += random.choice(all_characters)

password_list = list(password)
random.shuffle(password_list)

final_password = "".join(password_list)

print("Generated Password:", final_password)