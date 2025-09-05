# Write your solution here
def count_matching_elements(lst:list, x :int):
    c = 0
    for r in lst:
        for j in r:
            if j == x:
                c+= 1

    return c

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))