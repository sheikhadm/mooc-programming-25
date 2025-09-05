# Write your solution here
def greatest_number(x,y,z):
    great = x
    i = 0
    if great >= y and great >= z:
       return great
    elif great < y and y >= z:
       great = y
       return great
    elif great < z and z >= y:
       great = z
       return great
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)