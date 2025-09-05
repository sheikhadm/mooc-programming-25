# Write your solution here
items = int(input('How many items: '))
i = 1
lst = []
while i <= items:
    item = int(input(f'item {i}: '))
    lst.append(item)
    i += 1
print(lst)
