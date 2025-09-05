# Write your solution here
lst = []
while True:
    item = int(input('New Item: '))
    if item == 0:
        print('Bye!')
        break
    else:
       lst.append(item)
       print(f'The list now: {lst}')
       print(f'The list in order: {sorted(lst)}')
