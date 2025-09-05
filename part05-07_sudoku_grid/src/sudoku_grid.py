# Write your solution here
def sudoku_grid_correct(lst: list):
    i = 0
    j = 0
    while i < len(lst):
        while j < len(lst):
            if block_correct(lst, i, j) :
                j += 3
            else:
                return False
        i += 3
        j = 0
    ip = 0
    while ip < len(lst):
        if column_correct(lst, ip) and row_correct(lst , ip):
            ip += 1
        else: 
            return False
    return True

def row_correct(lst: list, rn : int):
    num = []
    for x in lst[rn]:
        if x > 0 and x < 10:
            if x in num:
                return False
            else:
                num.append(x)
    return True

def column_correct(lst: list, rn : int):
    num = []
    for j in lst:
        x = j[rn]
        if x > 0 and x < 10:
            if x in num:
                return False
            else:
                num.append(x)
    return True

def block_correct(lst : list, rn :int,cn :int):
#rn = row_no, cn = column no
    num = []
    i = rn + 3
    j = cn + 3
    x = rn
    y = cn
    while x < i:
        while y < j:
            p = lst[x][y]
            if p > 0 and p < 10:
                if p in num:
                    return False
                else:
                    num.append(p)
            y += 1
        x += 1
        y = cn
    return True



if __name__ == "__main__":
    sudoku1 =  [
    [ 2, 9, 5, 0, 8, 4, 7, 1, 3 ],
    [ 6, 4, 8, 1, 3, 7, 9, 2, 5 ],
    [ 1, 7, 3, 2, 0, 9, 4, 6, 8 ],
    [ 8, 6, 0, 3, 4, 1, 2, 5, 7 ],
    [ 5, 2, 7, 8, 9, 6, 0, 3, 4 ],
    [ 3, 1, 4, 0, 7, 2, 6, 8, 9 ],
    [ 7, 5, 0, 9, 2, 8, 1, 4, 0 ],
    [ 4, 3, 6, 7, 1, 5, 8, 0, 2 ],
    [ 0, 8, 0, 4, 6, 3, 5, 7, 1 ],
    ]

    print(sudoku_grid_correct(sudoku1))
    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

      