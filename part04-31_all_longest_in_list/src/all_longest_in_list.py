# Write your solution here
def all_the_longest(lst):
    lngs = []
    lng = 0
    for x in lst:
        if lng < len(x):
            lng = len(x)

    for x in lst:
        if len(x) == lng:
            lngs.append(x)

    return lngs

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result)
