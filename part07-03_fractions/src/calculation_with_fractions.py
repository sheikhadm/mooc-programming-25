# Write your solution here
from fractions import Fraction

def fractionate(d:int):
    lst = []
    for x in range(d):
        lst.append(Fraction(1,d))
    return lst
        


if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))