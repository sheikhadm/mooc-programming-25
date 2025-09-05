# Write your solution here
def times_ten(start_index: int, end_index: int):
    tt = {}
    for x in range(start_index, end_index + 1):
        tt[x] = x * 10
    return tt

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)


