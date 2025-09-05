# Write your solution here
def remove_smallest(numbers : list):
    small = numbers[0]
    for x in numbers:
        if x <= small:
            small = x
    numbers.remove(small)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)