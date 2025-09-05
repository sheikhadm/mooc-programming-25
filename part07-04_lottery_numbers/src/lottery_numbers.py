# Write your solution here
import random

def lottery_numbers(amount: int,lower:int ,upper:int):
    numbers = list(range(lower,upper + 1))
    random.shuffle(numbers)
    i = 0
    c = []
    while i < amount:
        c.append(numbers[i])
        i += 1
    return sorted(c)

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)