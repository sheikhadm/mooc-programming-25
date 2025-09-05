# Write your solution here
def shortest(lst):
    lng = len(lst[0])
    short = ''
    for x in lst:
        if len(x) <= lng:
            lng = len(x)
            short = x
    
    return short

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)

