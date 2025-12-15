# Write your solution here
import random

def roll(die: str):
    if die == "A":
        sides = [3, 3, 3, 3, 3, 6]
    elif die == "B":
        sides = [2, 2, 2, 5, 5, 5]
    elif die == "C":
        sides = [1, 4, 4, 4, 4, 4]
    else:
        return None

    return random.choice(sides)


def play(die1: str, die2: str, times: int):
    wins1 = 0
    wins2 = 0
    ties = 0

    for _ in range(times):
        r1 = roll(die1)
        r2 = roll(die2)

        if r1 > r2:
            wins1 += 1
        elif r2 > r1:
            wins2 += 1
        else:
            ties += 1

    return (wins1, wins2, ties)
