# Write your solution here
def mean(lst):
    sm =sum(lst)
    return sm / len(lst)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print('mean value is', result)