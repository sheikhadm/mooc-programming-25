# Write your solution here
def length_of_longest(lst):
    lng = 0
    for x in lst:
        if lng <= len(x):
            lng = len(x)
    return lng

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)