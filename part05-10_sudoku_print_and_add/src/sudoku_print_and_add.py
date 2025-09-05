# Write your solution here
def print_sudoku(sdk: list):
    i = 0
    j = 0
    while i < len(sdk):
        while j < len(sdk):
            if sdk[i][j] == 0:
               sdk[i][j] = '_'
            print(sdk[i][j], end = ' ')
            if j == 2 or j == 5 or j == 8:
                print(" ", end = "")
            j+= 1
        if i == 2 or i == 5 or i == 8:
                print(" ")
        i += 1
        j = 0
        print(' ')

def add_number(sdk:list , rn : int , cn:int,number:int):
    sdk[rn][cn] = number

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)