# Write your solution here
def sum_of_positives(lst):
    sm = 0
    for x in lst:
        if x > 0:
            sm = sm + x
    return sm

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
