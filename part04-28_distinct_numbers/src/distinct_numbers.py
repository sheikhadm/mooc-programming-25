# Write your solution here
def distinct_numbers(lst):
    ln = []
    for x in lst:
        if x in ln:
            continue
        else:
            ln.append(x)
    return sorted(ln)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))
