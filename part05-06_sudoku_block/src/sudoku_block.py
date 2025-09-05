# Write your solution here
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
    sudoku = [
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

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 6, 6))
