# Write your solution here
def who_won(lst: list):
    fp = 0
    sp = 0
    for r in lst:
        for j in r:
            if j == 1:
                fp += 1
            elif j == 2:
                sp += 1
    if fp > sp:
        return 1
    elif sp > fp:
        return 2
    else:
        return 0

