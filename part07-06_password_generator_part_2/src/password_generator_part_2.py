# Write your solution here
import string
import random

def generate_strong_password(x: int, n: bool, p: bool):
    letters = list(string.ascii_lowercase)
    num = list(string.digits)
    punc = ['!', '?', '=', '+', '-', '(', ')', '#']

    password_chars = []
    password_chars.append(random.choice(letters))
    # Guarantee at least one number if n is True
    if n:
        password_chars.append(random.choice(num))
    
    # Guarantee at least one punctuation if p is True
    if p:
        password_chars.append(random.choice(punc))
    
    # Fill the rest of the password
    while len(password_chars) < x:
        if n and p:
            pool = letters + num + punc
        elif n and not p:
            pool = letters + num
        elif p and not n:
            pool = letters + punc
        else:
            pool = letters
        password_chars.append(random.choice(pool))

    # Shuffle so guaranteed chars aren't always at start
    random.shuffle(password_chars)

    return ''.join(password_chars)

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(5, True, True))
