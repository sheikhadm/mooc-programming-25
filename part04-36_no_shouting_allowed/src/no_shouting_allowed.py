# Write your solution here
def no_shouting (lst):
    nm = []
    for x in lst:
        if not x.isupper():
            nm.append(x)
    return nm

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)

