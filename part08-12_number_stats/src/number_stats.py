# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if len(self.numbers) == 0:
            return 0
        return self.get_sum() / len(self.numbers)


# Create three NumberStats objects
stats_all = NumberStats()
stats_even = NumberStats()
stats_odd = NumberStats()

print("Please type in integer numbers:")

while True:
    num = int(input())

    if num == -1:
        break

    stats_all.add_number(num)

    if num % 2 == 0:
        stats_even.add_number(num)
    else:
        stats_odd.add_number(num)

print("Sum of numbers:", stats_all.get_sum())
print("Mean of numbers:", stats_all.average()) 
print("Sum of even numbers:", stats_even.get_sum())
print("Sum of odd numbers:", stats_odd.get_sum())
