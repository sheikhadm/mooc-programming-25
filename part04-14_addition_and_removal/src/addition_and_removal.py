# Write your solution here
lst = []
i = 0
while True:
    print(f'The list is now {lst}')
    ans = input('a(d)d, (r)emove or e(x)it: ')
    if ans == 'd':
        i += 1
        lst.append(i)
    elif ans == 'r':
        i -= 1
        lst.pop(i)
    elif ans == 'x':
        print('Bye!')
        break
    

