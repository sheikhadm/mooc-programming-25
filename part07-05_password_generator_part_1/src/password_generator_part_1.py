# Write your solution here
import string
import random

def generate_password(x:int):
    letters= list(string.ascii_lowercase)
    password = ''
    for x in range(x):
        password += random.choice(letters)
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
