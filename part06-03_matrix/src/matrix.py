# write your solution here
def matrix_sum():
    sm = 0
    with open('matrix.txt') as new_file:
        for line in new_file:
            line = line.replace('\n', '')
            parts = line.split(',')
            for x in parts:
                sm += int(x)
    
    return sm

def matrix_max():
    c = 0
    with open('matrix.txt') as new_file:
        for line in new_file:
            line = line.replace('\n', '')
            parts = line.split(',')
            for x in parts:
                if c < int(x):
                    c= int(x)
        return c

def row_sums():
    c = []
    with open('matrix.txt') as new_file:
        for line in new_file:
            line = line.replace('\n', '')
            parts = line.split(',')
            sm = 0
            for x in parts:
               sm += int(x)
            c.append(sm)
        return c
    
if __name__ == "__main__":
    print(row_sums())

# Calling row_sums() returns valuen
# [-1322, -1363, -946, -30, 558, 1589, 2469, 4217, 1796, 1318, 5094, 5440, 5749, 4868, 4542]
# correct answer is
# [-1322, -41, 417, 916, 588, 1031, 880, 1748, -2421, -478, 3776, 346, 309, -881, -326]