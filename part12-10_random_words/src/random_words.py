# Write your solution here:
import random 
def word_generator(characters:str, length:int,amount:int):
    num = 0
    random_word = ''
    while num < amount:
        yield "".join(random.choices(characters, k = length))
        num += 1

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)