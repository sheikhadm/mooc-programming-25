# Write your solution here
def everything_reversed(lst):
    i = len(lst) - 1
    nm = []
    while i >= 0:
        cn = lst[i]
        c = cn[::-1]
        nm.append(c)
        i -= 1
    return nm

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
