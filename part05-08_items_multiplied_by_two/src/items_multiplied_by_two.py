# Write your solution here
def double_items(lst: list):
    num = []
    for x in lst:
        c = x * 2
        num.append(c)
    return num

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)