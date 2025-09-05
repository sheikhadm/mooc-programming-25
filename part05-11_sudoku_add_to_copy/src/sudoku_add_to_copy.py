# Write your solution here
import copy
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
    return sdk

def copy_and_add(sdk,rn,cn,number):
    new_list = copy.deepcopy(sdk)
    new_list[rn][cn] = number
    return new_list

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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
