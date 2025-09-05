# Write your solution here
def create_tuple(x: int,y:int, z:int):
    smll = x
    great = x
    sm = 0
    bn = [x,y,z]
    for x in bn:
        if smll > x:
            smll = x
        if great < x:
            great= x
        sm += x
    return (smll,great,sm)

if __name__ == "__main__":
    print(create_tuple(1, 4, 2))