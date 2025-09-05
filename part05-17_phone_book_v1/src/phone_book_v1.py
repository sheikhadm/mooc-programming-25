# Write your solution here
book = {}
while True :
    cmd = int(input('command (1 search, 2 add, 3 quit): '))
    if cmd == 3 :
        print('quitting...')
        break
    elif cmd == 2:
        name = input('name: ')
        number = input('number: ')
        book[name] = number
        print('ok!')
    elif cmd == 1:
        name = input('name: ')
        if name not in book:
            print ('no number')
        else:
            print(book[name])
