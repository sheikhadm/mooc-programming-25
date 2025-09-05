# Write your solution here
def longest_series_of_neighbours(lst):
    i = 0
    num = 0
    neig = []
    while i < len(lst):
        if i != len(lst) - 1:
            c = i+ 1
            if lst[c] - lst[i] == 1 or lst[i] + 1 == lst[c] or lst[i] - lst[c] == 1:
                neig.append(lst[i])
                if len(neig) > num:
                    num = len(neig)
            else:
                neig = []
        i += 1
    return num + 1

if __name__ == "__main__":
    my_list = [1, 2, 5, 4, 3, 4]
    print(longest_series_of_neighbours(my_list))