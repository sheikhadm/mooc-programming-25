# Write your solution here
from math import sqrt
def hypotenuse(x:float, y:float):
    c= x * x
    d = y * y
    sm = c + d
    return sqrt(sm)

if __name__ == "__main__":
    print(hypotenuse(3,4)) # 5.0
    print(hypotenuse(5,12)) 
