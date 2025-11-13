# WRITE YOUR SOLUTION HERE:
def remove_smaller_than(number:list,limit:int):
    return [num for num in number if num >= limit]

if __name__ == "__main__":
    numbers = [1,65, 32, -6, 9, 11]
    print(remove_smaller_than(numbers, 10))