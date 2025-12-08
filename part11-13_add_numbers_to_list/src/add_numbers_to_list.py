# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers:list):
    if len(numbers) % 5 != 0:
        new_number = numbers[-1] + 1
        numbers.append(new_number)
    while len(numbers) % 5 != 0:
        add_numbers_to_list(numbers)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    add_numbers_to_list(numbers)
    print(numbers)

